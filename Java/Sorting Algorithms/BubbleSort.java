class BubbleSort {

    // Helpers
    static int[] swap(int[] arr, int index1, int index2) {
        int temp = arr[index2];
        arr[index2] = arr[index1];
        arr[index1] = temp;
        return arr;
    }

    static void printList(int[] lst) {
        for (int i : lst) {
            System.out.print(i + ", ");
        }
        System.out.println("");
    }

    // Bubble Sort
    static int[] bubbleSort(int[] arr) {

        for (int i = arr.length; i > 0; i--) {
            for (int j = 0; j < i-1; j++) {
                if (arr[j] > arr[j + 1]) {
                    swap(arr, j, j + 1);
                }
            }
        }
        return arr;

    }

    // Tests
    public static void main(String[] args) {
        int[] lst = { 2, 7, 1, 66, 33, 2, 9, 12, 15, 3, 2 };
        printList(lst);
        
        int [] result = bubbleSort(lst);
        printList(result);

    }
}