import java.util.*;
public class Day_37_sol {
    static class TreeNode {
        int val;
        TreeNode left, right;
        TreeNode(int val) {
            this.val = val;
        }
    }
    static void inOrderTraversal(TreeNode node, List<Integer> result) {
        if (node != null) {
            inOrderTraversal(node.left, result);
            result.add(node.val);
            inOrderTraversal(node.right, result);
        }
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] n = sc.nextLine().split("\\s+");
        if (n.length < 1){
        return;
        }
        TreeNode root = new TreeNode(Integer.parseInt(n[0]));
        if (n.length > 1){
            root.left = new TreeNode(Integer.parseInt(n[1]));
        }if (n.length > 2) {
            root.right = new TreeNode(Integer.parseInt(n[2]));
        }
        List<Integer> result = new ArrayList<>();
        inOrderTraversal(root, result);
        for (int i = 0; i < result.size(); i++) {
            if (i > 0) {
                System.out.print(" ");
            }
            System.out.print(result.get(i));
        }
    }
}
