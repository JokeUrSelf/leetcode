// https://leetcode.com/problems/add-two-numbers

/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function (l1, l2) {

    let ln = new ListNode(0, null);
    let lt = ln;
    let carry = 0;
    while ( l1 || l2 || carry) {
        const sum = (l1?.val || 0) + (l2?.val || 0) + carry;
        ln.next = new ListNode(sum % 10, null);
        carry = Math.floor(sum / 10);

        ln = ln.next;
        l1 = l1?.next;
        l2 = l2?.next;
    }
    return lt.next;
};
