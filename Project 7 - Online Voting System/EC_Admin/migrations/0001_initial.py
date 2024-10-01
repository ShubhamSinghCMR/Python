from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('candidate_id', models.CharField(max_length=10, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('father_name', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=6)),
                ('dateofbirth', models.DateField()),
                ('address', models.CharField(max_length=1024)),
                ('mobile_no', models.BigIntegerField()),
                ('state', models.CharField(max_length=50)),
                ('pincode', models.CharField(max_length=6)),
                ('constituency', models.CharField(max_length=50)),
                ('parliamentary', models.CharField(blank=True, max_length=50, null=True)),
                ('assembly', models.CharField(blank=True, max_length=50, null=True)),
                ('candidate_image', models.ImageField(upload_to='CandidateImage/')),
                ('candidate_party', models.CharField(max_length=50)),
                ('party_image', models.ImageField(upload_to='PartyImage/')),
                ('affidavit', models.FileField(null=True, upload_to='CandidateAffidavit/')),
            ],
        ),
        migrations.CreateModel(
            name='EC_Admins',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ecadmin_id', models.CharField(max_length=50, unique=True)),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('middlename', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=6)),
                ('dateofbirth', models.DateField()),
                ('address', models.CharField(max_length=1024)),
                ('pincode', models.CharField(max_length=6)),
                ('mobile_no', models.BigIntegerField(unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('ecadmin_image', models.ImageField(upload_to='ECAdminImage/')),
            ],
        ),
        migrations.CreateModel(
            name='Election',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('election_id', models.CharField(max_length=50, unique=True)),
                ('election_type', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('start_date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_date', models.DateField()),
                ('end_time', models.TimeField()),
                ('status', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Reports',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('election_id', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('constituency', models.CharField(max_length=50)),
                ('electors_male', models.BigIntegerField(default=0)),
                ('electors_female', models.BigIntegerField(default=0)),
                ('electors_others', models.BigIntegerField(default=0)),
                ('electors_total', models.BigIntegerField(default=0)),
                ('voters_male', models.BigIntegerField(default=0)),
                ('voters_female', models.BigIntegerField(default=0)),
                ('voters_others', models.BigIntegerField(default=0)),
                ('voters_total', models.BigIntegerField(default=0)),
                ('poll_male', models.FloatField()),
                ('poll_female', models.FloatField()),
                ('poll_others', models.FloatField()),
                ('poll_total', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Voters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voterid_no', models.CharField(max_length=10, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('father_name', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=6)),
                ('dateofbirth', models.DateField()),
                ('address', models.CharField(max_length=1024)),
                ('mobile_no', models.BigIntegerField()),
                ('state', models.CharField(max_length=50)),
                ('pincode', models.CharField(max_length=6)),
                ('parliamentary', models.CharField(max_length=50)),
                ('assembly', models.CharField(max_length=50)),
                ('voter_image', models.ImageField(upload_to='VoterImage/')),
            ],
        ),
        migrations.CreateModel(
            name='Votes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('election_id', models.CharField(max_length=50)),
                ('candidate_id', models.CharField(max_length=50)),
                ('candidate_name', models.CharField(max_length=100)),
                ('candidate_party', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('constituency', models.CharField(max_length=50)),
                ('online_votes', models.BigIntegerField(default=0)),
                ('evm_votes', models.BigIntegerField(default=0)),
                ('total_votes', models.BigIntegerField(default=0)),
            ],
        ),
    ]
