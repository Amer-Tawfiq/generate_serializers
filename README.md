# generate_serializers

A utility to auto-generate Django REST Framework serializers for all models in specified Django apps.

## Installation

You can install this package locally or from PyPI (if published):

```bash
pip install generate_serializers


"""
كيف تستخدم المكتبة؟
الخطوة 1: ضع مجلد generate_serializers في مكان معروف (مثلاً بجانب مشروعك أو داخل بيئة العمل)
الخطوة 2: ثبّت المكتبة محليًا (من داخل مجلد المكتبة)
pip install generate_serializers
الخطوة 3: استخدم المكتبة في مشروع Django الخاص بك
from generate_serializers import generate_serializers_for_apps

generate_serializers_for_apps(
    app_names=['my_app1', 'my_app2'],  # أسماء التطبيقات في مشروعك
    project_settings_module='my_project.settings'  # مسار إعدادات مشروع Django
)

"""