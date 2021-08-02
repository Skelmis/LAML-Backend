from django.contrib import admin

from .models import Event, Item, Player


@admin.action(description="Delete selected (No confirmation)")
def delete_selected_no_conf(modeladmin, request, queryset):
    queryset.delete()


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("slug", "item_type", "item_max", "title")
    search_fields = ("slug", "item_type", "item_max", "title", "description")
    actions = (delete_selected_no_conf,)


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ("get_slug", "get_event_pk", "username")
    search_fields = ("username",)

    def get_slug(self, player):
        return player.event.slug

    get_slug.short_description = "Event slug"

    def get_event_pk(self, player):
        return player.event.pk

    get_event_pk.short_description = "Event pk"

    actions = (delete_selected_no_conf,)


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("get_player_username", "get_event_slug", "amount")
    search_fields = ("get_player_username", "amount", "get_event_slug")

    def get_player_username(self, item):
        return item.player.username

    get_player_username.short_description = "Player username"

    def get_event_slug(self, item):
        return item.player.event.slug

    get_event_slug.short_description = "Event slug"
