import java.util.NoSuchElementException;

public interface QueueInterface {
    void push(int item);
    int pop() throws NoSuchElementException;
    int peek()  throws NoSuchElementException;
    int getLength();
    boolean isEmpty();
}