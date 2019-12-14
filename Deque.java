import java.util.NoSuchElementException;

public class Deque implements DequeInterface {
    private int[] items;
    public Deque(){
        this.items = new int[0];
    }

    public void pushLeft(int item) {
        int[] newarr = new int[this.items.length+1];
        int counter = 1;
        newarr[0] = item;
        for (int value : this.items) {
            newarr[counter] = value;
            counter++;
        }
        this.items = newarr;
    }

    public void pushRight(int item) {
        int[] newarr = new int[this.items.length+1];
        int counter = 0;
        newarr[this.items.length] = item;
        for (int value : this.items) {
            newarr[counter] = value;
            counter++;
        }
        this.items = newarr;
    }
    public int peekLeft() throws NoSuchElementException {
        if (this.items.length == 0) {
            throw new NoSuchElementException();
        }
        return this.items[0];
    }

    public int peekRight() throws NoSuchElementException {
        if (this.items.length == 0) {
            throw new NoSuchElementException();
        }
        return this.items[this.items.length-1];
    }

    public int popRight() throws NoSuchElementException {
        int item = this.peekRight();
        int[] newarr = new int[this.items.length-1];
        System.arraycopy(this.items, 0, newarr, 0, this.items.length - 1);
        this.items = newarr;
        return item;
    }

    public int popLeft() throws NoSuchElementException {
        int item = this.peekLeft();
        int[] newarr = new int[this.items.length-1];
        System.arraycopy(this.items, 1, newarr, 1, this.items.length - 1);
        this.items = newarr;
        return item;
    }
    public boolean isEmpty() {return this.items.length == 0;}
    public int getLength() {return this.items.length;}

}
