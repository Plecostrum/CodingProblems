public class App {
    public static void main(String[] args) throws Exception {
        int arr0[] = {9,5,8,10,7,8};
        int arr1[] = {9,11,8,5,7,10};
        int arr[] = {100, 180, 260, 310, 40, 535, 695};

        System.out.println(maxProfit(arr1));

    }

    private static int maxProfit(int[] array) {
        int buy = 0;
        int sell = 1;
        for (int i = sell; i < array.length; i++) {
            if (array[sell] < array[i]){
                sell++;
            }
            if (array[buy] > array[i]) {
                buy = i;
                sell = i+1;                 
            }
        }
        System.out.println("Most profit: "  + (array[sell] - array[buy]) + " buy index " + array[buy] + " sell index " + array[sell]);
        return (array[sell] - array[buy]);
    }
}
