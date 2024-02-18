# Generated by Django 4.1.13 on 2024-02-17 15:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('system_users_app', '0001_initial'),
        ('posts_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('commentId', models.AutoField(primary_key=True, serialize=False)),
                ('comment', models.CharField(max_length=255)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='posts_app.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='system_users_app.user')),
            ],
        ),
    ]