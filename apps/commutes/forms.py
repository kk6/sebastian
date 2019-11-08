from django import forms

from .appmodels import complete_stations
from .models import Commute
from .utils import CommuteUsageTypes
from .utils import dates_str_to_dates


class CommuteForm(forms.Form):
    """交通費の登録フォーム

    利用日はカンマ区切りで複数日入力可能

    """

    USAGE_CHOICES = ((1, "出社"), (2, "打ち合わせ"), (3, "その他"))
    ROUTE_CHOICES = ((1, "自宅〜会社"), (2, "その他"))
    usage_type = forms.TypedChoiceField(
        label="利用種別",
        choices=USAGE_CHOICES,
        widget=forms.RadioSelect,
        coerce=int,
        empty_value=None,
    )
    usage_text = forms.CharField(
        label="利用種別「その他」の場合に入力", max_length=255, required=False
    )
    route = forms.TypedChoiceField(
        label="経路",
        choices=ROUTE_CHOICES,
        widget=forms.RadioSelect,
        coerce=int,
        empty_value=None,
    )
    departure_station = forms.CharField(label="出発駅", max_length=255, required=False)
    arrival_station = forms.CharField(label="到着駅", max_length=255, required=False)
    date_of_use = forms.CharField(
        label="利用日",
        widget=forms.TextInput(
            attrs={
                "class": "input datepicker-here",
                "data-language": "en",
                "id": "datepicker",
                "data-multiple-dates": "true",
                "data-multiple-dates-separator": ",",
                "data-date-format": "yyyy/m/d",
                "autocomplete": "off",
                "data-position": "top left",
            }
        ),
    )
    price = forms.DecimalField(label="金額")
    is_round_trip = forms.BooleanField(label="往復？", required=False)
    has_apply = forms.BooleanField(label="申請済み？", required=False)

    def clean_usage_type(self):
        usage_type = self.cleaned_data.get("usage_type")
        return CommuteUsageTypes(usage_type)

    def clean(self):
        route = self.cleaned_data.pop("route")
        _departure_station = self.cleaned_data.get("departure_station")
        _arrival_station = self.cleaned_data.get("arrival_station")
        _date_of_use = self.cleaned_data.get("date_of_use")

        departure_station, arrival_station = complete_stations(
            route, _departure_station, _arrival_station
        )
        self.cleaned_data["departure_station"] = departure_station
        self.cleaned_data["arrival_station"] = arrival_station

        dates_of_use = dates_str_to_dates(_date_of_use)
        self.cleaned_data["date_of_use"] = dates_of_use

    def get_cleaned_results(self):
        fields = (
            "usage_type",
            "usage_text",
            "departure_station",
            "arrival_station",
            "date_of_use",
            "price",
            "is_round_trip",
            "has_apply",
        )
        results = []
        if self.is_valid():
            r = {f: self.cleaned_data[f] for f in fields}
            is_round_trip = r.pop("is_round_trip")
            for date_of_use in r["date_of_use"]:
                d = r.copy()
                d["date_of_use"] = date_of_use
                results.append(d)
                if is_round_trip:
                    c = d.copy()
                    c["departure_station"], c["arrival_station"] = (
                        d["arrival_station"],
                        d["departure_station"],
                    )
                    results.append(c)
            return results
        else:
            return None


class CommuteUpdateForm(forms.ModelForm):
    class Meta:
        model = Commute
        exclude = ("user",)
