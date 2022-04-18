from django.apps import AppConfig


class ProductsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.products'

    def ready(self) -> None:
        from .receivers import (
            product_create_update_notification,
            product_delete_notification,
            increment_product_view_counter
        )