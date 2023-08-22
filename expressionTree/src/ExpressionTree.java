import java.util.ArrayList;


public class ExpressionTree {

    Node root;

    public ExpressionTree(){
    }

    public int express(Node node){

        if(node == null){//Root is null
            return 0;   
        }

        if(node.left == null && node.right == null){
            //bottom is reached.
            return Integer.parseInt(node.value);
        }
        int left = express(node.left);
        int right = express(node.right);
        if(node.value == "+"){
            return left + right;
        }
        if(node.value == "*"){
            return left * right;
        }
        if(node.value == "/"){
            return left / right;
        }
        if(node.value == "-"){
            return left - right;
        }
        return 0;
    }

    public void orderTraverse(Node node){
        if (node != null){
            orderTraverse(node.left);
            System.out.print(node.value);
            orderTraverse(node.right);
        }
    }
}
