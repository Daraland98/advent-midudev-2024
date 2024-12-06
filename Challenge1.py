# Santa Claus 🎅 has received a list of magical numbers representing gifts 🎁, but some of them are duplicated and must be removed to avoid confusion. Additionally, the gifts must be sorted in ascending order before being delivered to the elves.

# Your task is to write a function that receives a list of integers (which may include duplicates) and returns a new list without duplicates, sorted in ascending order.

def prepare_gifts(gifts):
    unique_gifts = list(set(gifts))
    sorted_list = []
    for item in unique_gifts:
        low, high = 0, len(sorted_list)
        while low < high:
            mid = (low + high) // 2
            if sorted_list[mid] < item:
                low = mid + 1
            else:
                high = mid
        sorted_list.insert(low, item)
    
    return sorted_list



gifts1 = [3, 1, 2, 3, 4, 2, 5]
prepared_gifts1 = prepare_gifts(gifts1)
print(prepared_gifts1)  # [1, 2, 3, 4, 5]

gifts2 = [6, 5, 5, 5, 5]
prepared_gifts2 = prepare_gifts(gifts2)
print(prepared_gifts2)  # [5, 6]

gifts3 = []
prepared_gifts3 = prepare_gifts(gifts3)
print(prepared_gifts3)  # []




