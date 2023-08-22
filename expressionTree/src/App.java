public class App {
    public static void main(String[] args) throws Exception {
        System.out.println("Hello, World!");
        ExpressionTree tree = new ExpressionTree();

        Node root = new Node("*"); 
        root.left = new Node("*"); 
        root.left.left = new Node("3"); 
        root.left.right = new Node("*"); 
        root.left.right.left = new Node("4"); 
        root.left.right.right = new Node("5"); 
        root.right = new Node("+"); 
        root.right.left = new Node("4"); 
        root.right.right = new Node("5"); 

        tree.orderTraverse(root);
        System.out.println("");
        System.out.println(tree.express(root));
    }
}
