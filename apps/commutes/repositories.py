from decimal import Decimal
from typing import List
from typing import Optional
from typing import TYPE_CHECKING
from typing import Union

from django.db.models import QuerySet  # 下記コメント参照

from .models import Commute

# QuerySetについて::
#   型ヒントでしか使わないが、型検査時のみインポートにして
#     - 引用符で囲う -> flake8で警告
#     - そのまま -> djangoのシステムチェックに引っかかる
#   となるため常にインポートする
#   あと、reorder-python-importによってコメントとインポート文が引き離されるので
#   こういう「下記コメント参照」というような形式で分けてコメントしている

if TYPE_CHECKING:
    from datetime import date
    from .utils import CommuteUsageTypes


class CommuteRepository:
    """交通費のリポジトリ"""

    def __init__(self, model_commute=Commute):
        self.model_commute = model_commute

    def create_commute(
        self,
        usage_type: "CommuteUsageTypes",
        usage_text: Optional[str],
        departure_station: str,
        arrival_station: str,
        price: Decimal,
        date_of_use: "date",
        has_apply: bool,
        user_id: int,
    ) -> Commute:
        """交通費を作成する"""
        commute = self.model_commute(
            usage_type=usage_type,
            usage_text=usage_text,
            departure_station=departure_station,
            arrival_station=arrival_station,
            price=price,
            date_of_use=date_of_use,
            has_apply=has_apply,
            user_id=user_id,
        )
        commute.save()
        return commute

    def get_user_commutes(
        self, user_id: int, ordering: Optional[List[str]] = None
    ) -> Union[QuerySet, List[Commute]]:
        """ユーザーに紐づくすべての交通費"""
        return self.model_commute.objects.filter(user=user_id).order_by(*ordering)

    def get_user_commutes_monthly(self, user_id, year, month):
        """ユーザーに紐づく月ごとの交通費を取得する"""
        return self.model_commute.objects.filter(
            user=user_id, date_of_use__year=year, date_of_use__month=month
        )
