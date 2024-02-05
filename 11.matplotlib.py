import matplotlib.pyplot as plt
corruption_score=[1.850,1.248,1.072,1.159]
childlabour_percentage=[8.7,8.7,6.1,6.3]
plt.scatter(corruption_score,childlabour_percentage,color="blue",alpha=0.5)
plt.title("Perceived Corruption Score Vs ChildLabour Percentage.")
plt.xlabel("Perceived Corruption Score")
plt.ylabel("ChildLabour Percentage")
plt.show()