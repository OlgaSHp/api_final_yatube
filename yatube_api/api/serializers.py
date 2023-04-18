from posts.models import Comment, Follow, Group, Post, User
from rest_framework import serializers
from rest_framework.serializers import CurrentUserDefault


class PostSerializer(serializers.ModelSerializer):
    """Серилизатор постов."""

    author = serializers.SlugRelatedField(
        slug_field="username",
        read_only=True,
    )

    class Meta:
        model = Post
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    """Серилизатор комментариев."""

    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field="username",
    )

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ("post",)


class GroupSerializer(serializers.ModelSerializer):
    """Серилизатор групп."""

    class Meta:
        model = Group
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class FollowSerializer(serializers.ModelSerializer):
    """Серилизатор подписок."""

    user = serializers.SlugRelatedField(
        slug_field="username",
        read_only=True,
        default=CurrentUserDefault(),
    )
    following = serializers.SlugRelatedField(
        slug_field="username",
        read_only=False,
        queryset=User.objects.all(),
    )

    class Meta:
        model = Follow
        fields = '__all__'
        validators = (
            serializers.UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=("user", "following"),
                message="Вы уже подписаны на данного автора!",
            ),
        )

    def validate(self, data):
        if self.context["request"].user == data["following"]:
            raise serializers.ValidationError(
                "Вы не можете подписаться сам на себя!"
            )
        return data
