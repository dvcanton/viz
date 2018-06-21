library(plotly)

df <- read.csv("https://raw.githubusercontent.com/plotly/datasets/master/violin_data.csv")

p <- df %>%
  plot_ly(
    y = ~total_bill,
    type = 'violin',
    box = list(
      visible = T
    ),
    meanline = list(
      visible = T
    ),
    x0 = 'Total Bill'
  ) %>% 
  layout(
    yaxis = list(
      title = "",
      zeroline = F
    )
  )