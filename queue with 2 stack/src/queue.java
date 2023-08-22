import java.util.Stack;

public class queue<E> {

    private Stack<E> inbox = new Stack<>(); 
    private Stack<E> outbox = new Stack<>(); 

    public void enque(E item){
        inbox.push(item);
    }
    public E deque(){
        if (outbox.isEmpty()){
            while (!inbox.isEmpty()){
                outbox.push(inbox.pop());
            }
        }
        return outbox.pop();
    }
    
}

