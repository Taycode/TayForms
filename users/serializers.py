"""User Serializers"""

from dj_rest_auth.registration.serializers import RegisterSerializer


class CustomRegisterSerializer(RegisterSerializer):
	"""Custom Register Serializer"""

	username = None

	def update(self, instance, validated_data):
		"""
		:param instance:
		:param validated_data:
		:return:
		"""
		pass

	def create(self, validated_data):
		"""
		:param validated_data:
		:return:
		"""
		pass

