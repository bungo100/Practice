from collections import Counter
import heapq

def top_n_wit_heap(word_list, n):
    # d = {}
    # for word in word_list:
    #     d[word] = d.get(word, 0) + 1
    # print(d)

    counter_word = Counter(word_list)
    # print(Counter.most_common(counter_word, n))
    data = [(-counter_word[word], word) for word in counter_word]
    heapq.heapify(data)
    print([heapq.heappop(data)[1] for _ in range(n)])






if __name__ == '__main__':
    words = ['python', 'c', 'java', 'go', 'python', 'c', 'go', 'python']
    print(top_n_wit_heap(words, 3))


# numbers = [1,3,5,7,9,2,4,6,8,0]
# heap_data = []
#
# heapq.heapify(numbers)
# print(heapq.nlargest(3, numbers))
# print(heapq.nsmallest(3, numbers))

# for num in numbers:
#     heapq.heappush(heap_data, num)
#
# print(heap_data)
#
# while heap_data:
#     print(heapq.heappop(heap_data))