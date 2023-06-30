import seaborn as sb
import matplotlib.pyplot as plt
from pandas import *

df=read_csv("winequality-white.csv", sep=";")
print(df.keys())
# print(df["quality"].value_counts())#выводим категории качества и количество бутылок
# 6    2198
# 5    1457
# 7     880
# 8     175
# 4     163
# 3      20
# 9       5
ndf=df[(df["quality"] ==6) |
       (df["quality"] == 5) |
       (df["quality"] == 7)]
# print(ndf["quality"].value_counts())

#линейная зависимость:

#при снижении  количества остаточного сахара,качество вина растет
#sb.barplot(data=df, x=df["quality"], y=df["residual sugar"])

#явная зависимость,чем больше содержание алкоголя в вине,тем выше качество вина
#sb.barplot(data=df, x=df["quality"], y=df["alcohol"])

#при снижении  количества "chlorides",качество вина растет
# sb.barplot(data=df, x=df["quality"], y=df["chlorides"])

#при снижении  количества "total sulfur dioxide",качество вина растет
# sb.barplot(data=df, x=df["quality"], y=df["total sulfur dioxide"])

#линейная зависимость присутсвует,но  очень слабая("pH")
# sb.barplot(data=df, x=df["quality"], y=df["pH"])

#линейная зависимость присутсвует,но  очень слабая( при увеличении количества"sulphates" повышается качество)
# sb.barplot(data=df, x=df["quality"], y=df["sulphates"])

#линейная зависимость присутсвует,но очень слабая
# sb.lineplot(data=df, x=df["alcohol"],y=df["total sulfur dioxide"])

#прослеживается линейная зависимость, при уменьшении плотности вина повышается уровень алкоголя
# sb.lineplot(data=df, x=df["alcohol"],y=df["density"])

#прослеживается линейная зависимость,с большим количеством выбросов в промежутке 0-20 по стобцу residual sugar;0-1 о столбцу
#density. Итог: чем выше плотность, тем больше количество остаточного сахара
# sb.lineplot(data=df, x=df["residual sugar"],y=df["density"])

#линейная зависимость присутсвует total sulfur dioxide от free sulfur dioxide
# sb.lineplot(data=df, x=df["total sulfur dioxide"],y=df["free sulfur dioxide"])


# sb.heatmap(df.corr(),annot= True)


#fixed acidity находится в определенных пределах
# plt.subplot(2,2,1)
# df["fixed acidity"].plot.density()
# plt.subplot(2,2,2)
# df["fixed acidity"].plot.box()
# print(df[df["fixed acidity"]>8.7])

#линейной зависимости качества вина и "density" не прослеживается,находится в диапозоне 0.91 - 0.94
# sb.barplot(data=df, x=df["quality"], y=df["density"])

#зависимость качества от летучей кислотности не прослеживается
# sb.barplot(data=df, x=df["quality"], y=df["volatile acidity"])

#зависимость качества от "citric acid" не прослеживается
# sb.barplot(data=df, x=df["quality"], y=df["citric acid"])

#зависимость качества от "citric acid" не прослеживается
# sb.barplot(data=df, x=df["quality"], y=df["free sulfur dioxide"])


plt.show()

#Вывод:
# На качество вина влияют следующие показатели:
#"residual sugar"(количество остаточного сахара) при снижении уровня
#"alcohol"(содержание спирта) при увеличении уровня
#"chlorides"(хлоридов) при снижении уровня
#"total sulfur dioxide"(общий диоксид серы) при снижении уровня

