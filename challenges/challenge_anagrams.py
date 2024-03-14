def merge_sort(string, start=0, end=None):
    """Algoritmo de ordenação Merge Sort."""
    if end is None:
        end = len(string)
    if (end - start) > 1:  # se a lista tiver mais de um elemento
        mid = (start + end) // 2  # encontra o meio
        merge_sort(string, start, mid)  # dividindo as listas
        merge_sort(string, mid, end)
        merge(string, start, mid, end)  # unindo as listas
    return string


def merge(string, start, mid, end):
    """Função auxiliar do Merge Sort."""
    left = string[start:mid]  # indexando a lista da esquerda
    right = string[mid:end]  # indexando a lista da direita

    left_index, right_index = 0, 0  # as duas listas começarão do início

    for general_index in range(start, end):  # percorre a lista inteira
        if left_index >= len(left):
            string[general_index] = right[right_index]
            right_index = right_index + 1
        elif right_index >= len(right):
            string[general_index] = left[left_index]
            left_index = left_index + 1
        elif left[left_index] < right[right_index]:
            string[general_index] = left[left_index]
            left_index = left_index + 1
        else:
            string[general_index] = right[right_index]
            right_index = right_index + 1


def is_anagram(first_string, second_string):
    """Função que verifica se duas strings são anagramas."""
    # utiliza-se o list para transformar a string em um array de caracteres
    ordered_first_string = merge_sort(list(first_string.lower()))
    ordered_second_string = merge_sort(list(second_string.lower()))

    # utiliza-se o join para transformar o array de caracteres em uma string
    joined_first_string = ''.join(ordered_first_string)
    joined_second_string = ''.join(ordered_second_string)

    if not first_string or not second_string:
        return (joined_first_string, joined_second_string, False)
    else:
        compare_strings = joined_first_string == joined_second_string
        return (joined_first_string, joined_second_string, compare_strings)
