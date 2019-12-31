from pyecharts import charts
from pyecharts import options as opts
value=200
gu = charts.Gauge(init_opts=opts.InitOpts(width="640px", height="480px"))
gu.add("指标", [("昨日单位面积能耗", value)], split_number=10,
       axisline_opts=opts.AxisLineOpts(
           linestyle_opts=opts.LineStyleOpts(
               color=[(0.2, "#00B050"), (0.4, "#67e0e3"), (0.7, "#FF6600"), (1, "#fd666d")],
               width=25
           )
       ),
       min_=0,  # 最小刻度
       max_=1400,  # 最大刻度
       )
gu.set_global_opts(
    title_opts=opts.TitleOpts(title="楼宇能耗指标表盘\n昨日单位面积能耗{0}Wh/m^2".format(value)),
    legend_opts=opts.LegendOpts(is_show=False),
)
gu.render(r"C:\Users\CQ375\Desktop\ex\Guage-eg.html")
