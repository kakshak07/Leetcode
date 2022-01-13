class Solution {
    public ListNode swapPairs(ListNode head) {
        ListNode curr = head;
        ListNode prev = null;
        ListNode next = null;
        while (curr != null && curr.next != null) {
            next = curr.next;
            curr.next = next.next;
            next.next = curr;
            if (prev == null){
                head = next;
            } else {
                prev.next = next;
            }
            prev = curr;
            curr = curr.next;
        }
        return head;
    }
}