from rest_framework import serializers

from courses.models import Course, Lesson, Tag, Comment, Category, User, Action, Rating, LessonView

class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = User(**validated_data);
        user.set_password(user.password);
        user.save();
        return user;

    class Meta:
        model = User;
        fields = ["id", "first_name", "last_name","username", "password", "email", "date_joined"];
        extra_kwargs = {
            'password': {'write_only': 'true'}
        }  


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category;
        fields = "__all__";

class CourseSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField();

    def get_image(self, course):
        # Đối tượng request thường bỏ trong context và gửi qua serializer
        request = self.context['request'];
        name = course.image.name;
        if name.startswith("static/"):
            path = '%s' % name;
        else:
            path = '/static/%s' %name;
        return request.build_absolute_uri(path);

    class Meta:
        model = Course;
        fields = ['id', 'subject', 'created_date', 'image', 'category'];

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag;
        fields = '__all__';

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson;
        fields = ["id", "subject", "image", "created_date","updated_date", "course"];

class LessonDetailSerializer(LessonSerializer):
    tags = TagSerializer(many=True);

    class Meta:
        model = LessonSerializer.Meta.model;
        fields = LessonSerializer.Meta.fields + ['content', 'tags'];

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment;
        fields = ['id', 'content', 'created_date', 'updated_date'];

class ActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Action;
        fields = ['id', 'type', 'created_date'];

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating;
        fields = ['id', 'rate', 'created_date'];

class LessonViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonView;
        fields = ['id', 'views', 'lesson', 'created_date'];