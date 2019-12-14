import java.util.NoSuchElementException;

public class Queue implements QueueInterface {
    private int[] items;
    private int pointer;
    public Queue(){
        this.items = new int[0];
        this.pointer = -1;
    }

    public void push(int item) {
        int[] newarr = new int[this.items.length+1];
        int counter = 1;
        newarr[0] = item;
        for (int value : this.items) {
            newarr[counter] = value;
            counter++;
        }
        this.items = newarr;
    }


    public int peek() throws NoSuchElementException {
        if (this.items.length == 0) {
            throw new NoSuchElementException();
        }
        return this.items[this.items.length - this.pointer];
    }


    public int pop() throws NoSuchElementException {
        int item = this.peek();
        int[] newarr = new int[this.items.length-1];
        System.arraycopy(this.items, 1, newarr, 0, this.items.length - 1);
        this.items = newarr;
        return item;
    }
    public boolean isEmpty() {return this.pointer == -1;}
    public int getLength() {return this.pointer +1;}

}
