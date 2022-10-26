from django import forms
#from trade.models import Estimate
from .models import Estimate


class EstimateForm(forms.ModelForm):
    class Meta:
        model = Estimate
        """fields = ['estimate_id', 'buyer_id', 'project_name', 'material', 'method', 'pieces', 'detail', 'drawing']
        labels = {
            'estimate_id': '견적ID',
            'buyer_id': '구매자ID',
            'project_name': '프로젝트명',
            'material': '재료',
            'method': '가공방식',
            'pieces': '수량',
            'detail': '후가공',
            'drawing': '도면',
        }"""

        fields = ['project_name', 'material', 'method', 'pieces', 'detail', 'drawing']
        labels = {
            'project_name': '프로젝트명',
            'material': '재료',
            'method': '가공방식',
            'pieces': '수량',
            'detail': '후가공',
            'drawing': '도면',
        }
