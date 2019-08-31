from rest_framework import serializers
from recipe.models import Recipe, Ingredient, Step


class IngredientSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Ingredient
        fields = ('text', 'id', )


class StepSerializer(serializers.ModelSerializer):
    """ Step serializer """
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Step
        fields = ('step_text', 'id')


class RecipeSerializer(serializers.ModelSerializer):
    """Serialize a recipe"""
    user = serializers.StringRelatedField()
    ingredient = IngredientSerializer(many=True)
    step = StepSerializer(many=True)

    class Meta:
        model = Recipe
        fields = (
            'id', 'name', 'user', 'ingredient', 'step'
        )
        read_only_fields = ('id',)

    def create(self, validated_data):
        ingredient_recs = validated_data.pop('ingredient')
        step_recs = validated_data.pop('step')
        user = None
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user
        recipe = Recipe.objects.create(user=user, **validated_data)
        for ingredient_rec in ingredient_recs:
            Ingredient.objects.create(**ingredient_rec, recipe=recipe)
        for step_rec in step_recs:
            Step.objects.create(**step_rec, recipe=recipe)
        return recipe

    def update(self, instance, validated_data):
        user = None
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user
        instance.name = validated_data.get('name', instance.name)
        instance.user = user
        instance.save()
        ingredients = validated_data.get('ingredient')
        steps = validated_data.get('step')
        for ingredient in ingredients:
            ingredients_id = ingredient.get('id', None)
            if ingredients_id:
                ingredient_rec = Ingredient.objects.get(id=ingredients_id, recipe=instance)
                ingredient_rec.text = ingredient.get('text', ingredient_rec.text)
                ingredient_rec.save()
            else:
                Ingredient.objects.create(recipe=instance, **ingredient)
        for step in steps:
            step_id = step.get('id', None)
            if step_id:
                step_rec = Step.objects.get(id=step_id, recipe=instance)
                step_rec.step_text = step.get('step_text', step_rec.step_text)
                step_rec.save()
            else:
                Step.objects.create(recipe=instance, **step)
        return instance
