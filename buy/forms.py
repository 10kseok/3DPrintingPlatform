from django import forms
from trade.models import Estimate


class EstimateForm(forms.ModelForm):
    class Meta:
        model = Estimate
        fields = ['project_name', 'material', 'method', 'pieces', 'detail', 'drawing']
        labels = {
            'project_name': '프로젝트명',
            'material': '재료',
            'method': '가공방법',
            'pieces': '수량',
            'detail': '후처리',
            'drawing': '도면',
        }
