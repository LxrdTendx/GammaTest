def find_zero_product_triplets(nums):
    # Поиск индексов всех нулей в списке
    zero_indices = {i for i, num in enumerate(nums) if num == 0}

    # Множество для хранения уникальных триплетов в виде кортежей
    triplets_set = set()

    # Если в списке менее трех нулей, добавляем триплеты с нулями
    if len(zero_indices) > 0:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                # Убедимся, что i, j не равны и не указывают на ноль
                if i != j and i not in zero_indices and j not in zero_indices:
                    # Для каждого нуля формируем уникальный триплет
                    for zero_index in zero_indices:
                        # Создаем упорядоченный кортеж для уникальности
                        triplet = tuple(sorted([nums[i], nums[j], nums[zero_index]]))
                        triplets_set.add(triplet)

    # Преобразуем кортежи обратно в списки
    result = [list(triplet) for triplet in triplets_set]

    return result


# Пример ввода
nums = [1, 2, 0, 3, 0, 4]
# Вызов функции и вывод результата
result = find_zero_product_triplets(nums)
print("Output:", result)
