from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Complain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voterid_no', models.CharField(max_length=10)),
                ('complain', models.CharField(max_length=5000)),
                ('complain_reply', models.CharField(max_length=5000, null=True)),
                ('viewed', models.BooleanField(default=False)),
                ('replied', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Voted',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('election_id', models.CharField(max_length=50)),
                ('voter_id', models.CharField(max_length=10)),
                ('state', models.CharField(max_length=50)),
                ('constituency', models.CharField(max_length=50)),
                ('has_voted', models.CharField(max_length=3)),
                ('where_voted', models.CharField(max_length=7, null=True)),
                ('ipaddress', models.GenericIPAddressField(null=True)),
                ('datetime', models.DateTimeField(null=True)),
            ],
        ),
    ]
