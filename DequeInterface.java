import java.util.NoSuchElementException;

public interface DequeInterface {
    void pushLeft(int item);
    void pushRight(int item);
    int popLeft() throws NoSuchElementException;
    int popRight() throws NoSuchElementException;
    int peekLeft()  throws NoSuchElementException;
    int peekRight() throws NoSuchElementException;
    int getLength();
    boolean isEmpty();
}
