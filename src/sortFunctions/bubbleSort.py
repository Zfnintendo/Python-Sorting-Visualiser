from GUI.SortGUI import SortGUI
GUIHandler = SortGUI()

class BubbleSort:

    def Sort(self, arr):

        n = len(arr)

        for i in range(n-1):
            for j in range(n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    GUIHandler.UpdateGraph(UpdatedArray=arr)

        return arr
