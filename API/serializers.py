from rest_framework import serializers
from django.db.models import Sum
from abex.models import User, Transaction, TypeOfService


class UserSerializers(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'point']

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data.get('password'))
        user.save()
        return user


class TransactionSerializers(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = ['author', 'type_of_service', 'status']

    def create(self, validated_data):
        user = User.objects.get(username=self.validated_data.get('author'))
        if self.validated_data.get('status') == 'write-off':
            user.point -= self.validated_data.get('type_of_service').point
            if user.point == 0:
                print('0')
        else:
            user.point += self.validated_data.get('type_of_service').point
            print(User.objects.all().aggregate(Sum('point')))
            if user.point > 1000:
                print('1000+')
        user.save()
        return super(TransactionSerializers, self).create(validated_data)


class TypeOfServiceSerializers(serializers.ModelSerializer):

    class Meta:
        model = TypeOfService
        fields = ['name', 'point']
