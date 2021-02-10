public static int indexOfHighest(int[] arr) {
    int highestVal = arr[0];
    int highestInd = 0;
    
    for (int i = 0; i < arr.Length; i++) {
        if (arr[i] > highestVal) {
            highestVal = arr[i];
            highestInd = i;
        }
    }
    
    return highestInd
    
}