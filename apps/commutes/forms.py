from django import forms


class CommuteForm(forms.Form):
    """交通費の登録フォーム

    利用日はカンマ区切りで複数日入力可能

    """

    USAGE_CHOICES = ((1, "出社"), (2, "打ち合わせ"), (3, "その他"))
    ROUTE_CHOICES = ((1, "自宅〜会社"), (2, "その他"))
    usage_type = forms.ChoiceField(
        label="利用種別", choices=USAGE_CHOICES, widget=forms.RadioSelect
    )
    usage_text = forms.CharField(
        label="利用種別「その他」の場合に入力", max_length=255, required=False
    )
    route = forms.ChoiceField(
        label="経路", choices=ROUTE_CHOICES, widget=forms.RadioSelect
    )
    departure_station = forms.CharField(label="出発駅", max_length=255, required=False)
    arrival_station = forms.CharField(label="到着駅", max_length=255, required=False)
    date_of_use = forms.CharField(
        label="利用日",
        widget=forms.TextInput(
            attrs={
                "class": "datepicker-here",
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

    def get_cleaned_results(self):
        fields = (
            "usage_type",
            "usage_text",
            "route",
            "departure_station",
            "arrival_station",
            "date_of_use",
            "price",
            "is_round_trip",
            "has_apply",
        )
        if self.is_valid():
            return {f: self.cleaned_data[f] for f in fields}
        else:
            return {f: None for f in fields}
