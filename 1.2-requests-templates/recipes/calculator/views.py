from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


def recipe_view(request, dish_name):
    # Получаем рецепт из DATA
    recipe = DATA.get(dish_name)

    # Если рецепта нет, возвращаем 404
    if recipe is None:
        raise Http404(f"Рецепт '{dish_name}' не найден")

    # Получаем параметр servings (количество порций) из запроса, по умолчанию - 1
    servings = request.GET.get('servings', 1)

    try:
        servings = int(servings)
        if servings < 1:
            raise ValueError
    except ValueError:
        raise Http404("Количество порций должно быть положительным целым числом")

    # Умножаем количество ингредиентов на количество порций
    updated_recipe = {ingredient: amount * servings for ingredient, amount in recipe.items()}

    # Формируем контекст для передачи в шаблон
    context = {
        'recipe': updated_recipe
    }

    # Рендерим результат в шаблон
    return render(request, 'calculator/index.html', context)
