public class ArrayOperations {
    public static int[] extend(int[] arr) {
        int delta = arr.length/2 +1;
        int[] newarr = new int[arr.length+delta];
        for (int i = 0; i < arr.length; i++) {
            newarr[i] = arr[i];
        }
        return newarr;
    }


}
