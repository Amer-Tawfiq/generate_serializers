import os
import django
from django.apps import apps

def generate_serializers_for_apps(app_names, project_settings_module='my_project.settings'):
    """
    توليد ملفات serializers لكل التطبيقات المحددة

    :param app_names: قائمة أسماء التطبيقات (List[str])
    :param project_settings_module: اسم ملف إعدادات Django (str)
    """
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", project_settings_module)
    django.setup()

    for app_name in app_names:
        print(f"Generating serializers for app: {app_name}")

        try:
            app_models = apps.get_app_config(app_name).get_models()
        except LookupError:
            print(f"App {app_name} not found or not in INSTALLED_APPS")
            continue

        serializers_dir = os.path.join(app_name, 'serializers')
        os.makedirs(serializers_dir, exist_ok=True)

        init_file = os.path.join(serializers_dir, '__init__.py')
        if not os.path.exists(init_file):
            with open(init_file, 'w', encoding='utf-8') as f:
                f.write("# Auto-generated serializers package\n")

        for model in app_models:
            model_name = model.__name__
            file_name = f"{model_name.lower()}_serializer.py"
            file_path = os.path.join(serializers_dir, file_name)

            if os.path.exists(file_path):
                print(f"Skipping existing file: {file_name}")
                continue

            content = f"""from rest_framework import serializers
from ..models import {model_name}

class {model_name}Serializer(serializers.ModelSerializer):
    class Meta:
        model = {model_name}
        fields = '__all__'
"""

            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)

            print(f"Created: {file_path}")

    print("Done generating serializers.")
