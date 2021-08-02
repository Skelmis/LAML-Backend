# Generated by Django 3.2.6 on 2021-08-02 10:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_player_unique_together'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='player_username',
            new_name='player',
        ),
        migrations.RenameField(
            model_name='player',
            old_name='event_pk',
            new_name='event',
        ),
        migrations.AlterUniqueTogether(
            name='player',
            unique_together={('event', 'username')},
        ),
    ]