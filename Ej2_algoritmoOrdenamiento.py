

def merge_Sort(numbers):
    if len(numbers) > 1:
        center = len(numbers) // 2
        first_Half = numbers[:center]
        secong_Half = numbers[center:]

        merge_Sort(first_Half)
        merge_Sort(secong_Half)

    
