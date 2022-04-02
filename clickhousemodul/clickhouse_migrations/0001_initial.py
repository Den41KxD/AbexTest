from django_clickhouse import migrations
from clickhousemodul.clickhouse_models import ClickHouseUser, ClickhousePoint

class Migration(migrations.Migration):
    operations = [
        migrations.CreateTable(ClickHouseUser),
        migrations.CreateTable(ClickhousePoint)
    ]