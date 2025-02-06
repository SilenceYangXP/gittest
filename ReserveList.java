/**
 * ListNode类表示链表中的一个节点，包含一个整数值和指向下一个节点的指针。
 */
class ListNode {
    int val;
    ListNode next;

    ListNode(int x) {
        val = x;
        next = null;
    }
}

/**
 * ReserveList类包含主方法和用于反转链表及打印链表的方法。
 */
public class ReserveList {
    public static void main(String[] args) {
        // 创建一个链表: 1 -> 2 -> 3 -> 4 -> 5
        ListNode head = new ListNode(1);
        head.next = new ListNode(2);
        head.next.next = new ListNode(3);
        head.next.next.next = new ListNode(4);
        head.next.next.next.next = new ListNode(5);

        // 反转链表
        ListNode reversedHead = reverseList(head);

        // 打印反转后的链表
        printList(reversedHead);

        // 边界测试: 空链表
        ListNode emptyHead = null;
        printList(reverseList(emptyHead)); // 应该输出空
    }

    /**
     * 反转给定的链表并返回新的头节点。
     * @param head 链表的头节点
     * @return 反转后的链表的头节点
     */
    public static ListNode reverseList(ListNode head) {
        ListNode prev = null;
        ListNode current = head;

        while (current != null) {
            ListNode nextTemp = current.next; // 保存下一个节点
            current.next = prev;               // 反转当前节点的指针
            prev = current;                    // 移动 prev 和 current
            current = nextTemp;
        }
        return prev; // prev 将是新的头节点
    }

    /**
     * 打印链表的所有节点值，如果链表为空则输出提示信息。
     * @param head 链表的头节点
     */
    public static void printList(ListNode head) {
        if (head == null) {
            System.out.println("链表为空");
            return;
        }
        ListNode current = head;
        while (current != null) {
            System.out.print(current.val);
            current = current.next;
            if (current != null) {
                System.out.print(" -> "); // 仅在当前节点后面有下一个节点时打印箭头
            }
        }
        System.out.println(); // 打印完后换行
    }
} 