class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


def print_list(head):
    current_node = head
    while current_node:
        print(current_node.data, end=" -> ")
        current_node = current_node.next
    print("None")


def reverse_linked_list(head):
    prev_node = None
    current_node = head
    while current_node:
        next_node = current_node.next
        current_node.next = prev_node
        prev_node = current_node
        current_node = next_node
    return prev_node


def insertion_sort_linked_list(head):
    if not head or not head.next:
        return head

    sorted_head = None
    current_node = head

    while current_node:
        next_node = current_node.next
        sorted_head = insert_into_sorted(sorted_head, current_node)
        current_node = next_node

    return sorted_head


def insert_into_sorted(sorted_head, new_node):
    if not sorted_head or sorted_head.data >= new_node.data:
        new_node.next = sorted_head
        return new_node

    current_node = sorted_head
    while current_node.next and current_node.next.data < new_node.data:
        current_node = current_node.next

    new_node.next = current_node.next
    current_node.next = new_node

    return sorted_head


def merge_sorted_lists(list1, list2):
    dummy = Node()
    current_node = dummy

    while list1 and list2:
        if list1.data < list2.data:
            current_node.next = list1
            list1 = list1.next
        else:
            current_node.next = list2
            list2 = list2.next

        current_node = current_node.next

    current_node.next = list1 or list2

    return dummy.next


if __name__ == "__main__":
    input_list1 = list(map(int, input("Введіть елементи першого списку через пробіл: ").split()))
    head1 = Node(input_list1[0])
    current_node_main = head1
    for item in input_list1[1:]:
        current_node_main.next = Node(item)
        current_node_main = current_node_main.next

    input_list2 = list(map(int, input("Введіть елементи другого списку через пробіл: ").split()))
    head2 = Node(input_list2[0])
    current_node_main = head2
    for item in input_list2[1:]:
        current_node_main.next = Node(item)
        current_node_main = current_node_main.next

    reversed_head1 = reverse_linked_list(head1)
    print("Реверсований перший список: ")
    print_list(reversed_head1)

    sorted_head1 = insertion_sort_linked_list(reversed_head1)
    print("Відсортований перший список: ")
    print_list(sorted_head1)

    reversed_head2 = reverse_linked_list(head2)
    print("Реверсований другий список: ")
    print_list(reversed_head2)

    sorted_head2 = insertion_sort_linked_list(reversed_head2)
    print("Відсортований другий список: ")
    print_list(sorted_head2)

    merged_head = merge_sorted_lists(sorted_head1, sorted_head2)
    print("Об'єднаний відсортований список: ")
    print_list(merged_head)
