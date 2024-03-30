#Multi_layer_perceptron



#Input layer
a1 = 0.4 # int(input("Enter a number has your input"))
a2 = 0.3 # 
a3 = 0.7 # 
a4 = 0.6 # 


#HIDDEN LAYER 1-----------------------------------------------------------------
print("Hidden layer 2 Perceptrons")

#Weight of Layer 1 perceptron 1
w1_1_1 = 0.5
w1_1_2 = 0.10
w1_1_3 = 0.15
w1_1_4 = 0.20
w1_1_5 = 0.25

#Weight of Layer 1 perceptron 2
w1_2_6 = 0.30
w1_2_7 = 0.35
w1_2_8 = 0.40
w1_2_9 = 0.45
w1_2_10 = 0.50

#Weight of Layer 1 perceptron 3
w1_3_11 = 0.55
w1_3_12 = 0.60
w1_3_13 = 0.65
w1_3_14 = 0.70
w1_3_15 = 0.75

#Weight of Layer 1 perceptron 4
w1_4_16 = 0.80
w1_4_17 = 0.85
w1_4_18 = 0.90
w4_19 = 0.95
w1_4_20 = 1


#hidden_layer_1_perceptron_1
h1_c1 = (a1 * w1_1_1) + (a2 * w1_2_6) + (a3 * w1_3_11) + (a4 * w1_4_16)
print(f"hidden_layer_1_perceptron_1: {h1_c1}")

#hidden_Layer_1_perceptron_2
h1_c2 =  (a1 * w1_1_2) + (a2 * w1_2_7) + (a3 * w1_3_12) + (a4 * w1_4_17)
print(f"hidden_layer_2_perceptron_2: {h1_c2} ")

#hidden_Layer_1_perceptron_3
h1_c3 =  (a1 * w1_1_3) + (a2 * w1_2_8) + (a3 * w1_3_13) + (a4 * w1_4_18)
print(f"hidden_layer_1_perceptron_3: {h1_c3}")

#hidden_Layer_1_perceptron_4
h1_c4 =  (a1 * w1_1_4) + (a2 * w1_2_9) + (a3 * w1_3_14) + (a4 * w4_19)
print(f"hidden_layer_1_perceptron_4: {h1_c4}")

#hidden_Layer_1_perceptron_5
h1_c5 =  (a1 * w1_1_5) + (a2 * w1_2_10) + (a3 * w1_3_15) + (a4 * w1_4_20)
print(f"hidden_layer_1_perceptron_5: {h1_c5}")

#output_layer_3
final_result_layer1 = (h1_c1 + h1_c2 + h1_c3 + h1_c4 + h1_c5)
print(f"the final output of layer 1 is : {final_result_layer1}")

#HIDDEN LAYER 2-----------------------------------------------------------------

print("\nHidden player 2 Perceptrons")
#Weight of Layer 2 perceptron 1
w2_1_1 = 1.5
w2_1_2 = 1.10
w2_1_3 = 1.15
w2_1_4 = 1.20
w2_1_5 = 1.25

#Weight of Layer 2 perceptron 2
w2_2_6 = 1.30
w2_2_7 = 1.35
w2_2_8 = 1.40
w2_2_9 = 1.45
w2_2_10 = 1.50

#Weight of Layer 2 perceptron 3
w2_3_11 = 1.55
w2_3_12 = 1.60
w2_3_13 = 1.65
w2_3_14 = 1.70
w2_3_15 = 1.75

#Weight of Layer 2 perceptron 4
w2_4_16 = 1.80
w2_4_17 = 1.85
w2_4_18 = 1.90
w2_4_19 = 1.95
w2_4_20 = 2


#hidden_layer_2_perceptron_1
h2_c1 = (h1_c1 * w2_1_1) + (h1_c2 * w2_2_6) + (h1_c3 * w2_3_11) + (h1_c4 * w2_4_16)
print(f"hidden_layer_2_perceptron_1: {h2_c1}")

#hidden_Layer_2_perceptron_2
h2_c2 =  (h1_c1 * w2_1_2) + (h1_c2 * w2_2_7) + (h1_c3 * w2_3_12) + (h1_c4 * w2_4_17)
print(f"hidden_layer_2_perceptron_2: {h2_c2} ")

#hidden_Layer_2_perceptron_3
h2_c3 =  (h1_c1 * w2_1_3) + (h1_c2 * w2_2_8) + (h1_c3 * w2_3_13) + (h1_c4 * w2_4_18)
print(f"hidden_layer_2_perceptron_3: {h2_c3}")

#hidden_Layer_2_perceptron_4
h2_c4 =  (h1_c1 * w2_1_4) + (h1_c2 * w2_2_9) + (h1_c3 * w2_3_14) + (h1_c4 * w2_4_19)
print(f"hidden_layer_2_perceptron_4: {h2_c4}")

#hidden_Layer_2_perceptron_5
h2_c5 =  (h1_c1 * w2_1_5) + (h1_c2 * w2_2_10) + (h1_c3 * w2_3_15) + (h1_c4 * w2_4_20)
print(f"hidden_layer_2_perceptron_5: {h2_c5}")

#output_layer_2
final_result_layer2 = (h2_c1 + h2_c2 + h2_c3 + h2_c4 + h2_c5)
print(f"the final output of layer 2 is : {final_result_layer2}")

#HIDDEN LAYER 3 -----------------------------------------------------------------

print("\nHidden player 3 Perceptrons")
#Weight of Layer 3 perceptron 1
w3_1_1 = 2.5
w3_1_2 = 2.10
w3_1_3 = 2.15
w3_1_4 = 2.20
w3_1_5 = 2.25

#Weight of Layer 3 perceptron 2
w3_2_6 = 2.30
w3_2_7 = 2.35
w3_2_8 = 2.40
w3_2_9 = 2.45
w3_2_10 = 2.50

#Weight of Layer 3 perceptron 3
w3_3_11 = 2.55
w3_3_12 = 2.60
w3_3_13 = 2.65
w3_3_14 = 2.70
w3_3_15 = 2.75

#Weight of Layer 3 perceptron 4
w3_4_16 = 2.80
w3_4_17 = 2.85
w3_4_18 = 2.90
w3_4_19 = 2.95
w3_4_20 = 3


#hidden_layer_3_perceptron_1
h3_c1 = (h2_c1 * w3_1_1) + (h2_c2 * w3_2_6) + (h2_c3 * w3_3_11) + (h2_c4 * w3_4_16)
print(f"hidden_layer_3_perceptron_1: {h3_c1}")

#hidden_Layer_3_perceptron_2
h3_c2 =  (h2_c1 * w3_1_2) + (h2_c2 * w3_2_7) + (h2_c3 * w3_3_12) + (h2_c4 * w3_4_17)
print(f"hidden_layer_3_perceptron_2: {h3_c2} ")

#hidden_Layer_3_perceptron_3
h3_c3 =  (h2_c1 * w3_1_3) + (h2_c2 * w3_2_8) + (h2_c3 * w3_3_13) + (h2_c4 * w3_4_18)
print(f"hidden_layer_3_perceptron_3: {h3_c3}")

#hidden_Layer_3_perceptron_4
h3_c4 =  (h2_c1 * w3_1_4) + (h2_c2 * w3_2_9) + (h2_c3 * w3_3_14) + (h2_c4 * w3_4_19)
print(f"hidden_layer_3_perceptron_4: {h3_c4}")

#hidden_Layer_3_perceptron_5
h3_c5 =  (h2_c1 * w3_1_5) + (h2_c2 * w3_2_10) + (h2_c3 * w3_3_15) + (h2_c4 * w3_4_20)
print(f"hidden_layer_3_perceptron_5: {h3_c5}")

#<---------------------------------------------------------------------------------------------->
#output_layer_3
final_result_layer3 = (h3_c1 + h3_c2 + h3_c3 + h3_c4 + h3_c5)
print(f"the final output of layer 3 is : {final_result_layer3}")

