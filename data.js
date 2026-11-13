window.SITE_DATA = {
 "site": {
  "name": "复习资料库",
  "subtitle": "Study Hub · 按科目分类的复习站点",
  "owner": "",
  "updated": "2026-11-13"
 },
 "subjects": [
  {
   "code": "linear-algebra",
   "name": "线性代数",
   "en": "Matrices and Linear Algebra",
   "course": "MATH 0280",
   "term": "2026 Fall",
   "teacher": "Guanqiang (Tim) Zhou · Sichuan University – Auckland Institute",
   "color": "#2f6f9f",
   "accent": "blue",
   "scope": [
    "§2.1 线性方程组入门",
    "§2.2 直接法（高斯消元）",
    "§2.3 张成集与线性无关",
    "§3.1 矩阵运算",
    "§3.2 矩阵代数",
    "§3.3 矩阵的逆",
    "§3.5 子空间（只考 subspace）"
   ],
   "exclude": [
    "基 / 维数 / 秩的计算",
    "行列式",
    "特征值"
   ],
   "notes": "期中范围由老师明确：3.5 只考子空间；其余按章节计分。",
   "docs": [
    {
     "id": "midterm",
     "title": "期中冲刺 · 考点版",
     "file": "midterm/index.html",
     "full": "midterm-full.html",
     "desc": "按考试范围重排的七节考点：定义/定理/算法/例题、九类题型模板、速查表、易错点、60 分钟模拟卷（含答案）。",
     "tags": [
      "期中",
      "考点",
      "模拟卷"
     ],
     "date": "2026-10-30",
     "pages": 22,
     "pdf": "MATH0280_期中冲刺_手机版.pdf",
     "img": "mindmap-la-exam.png",
     "keywords": "2.1 2.2 2.3 3.1 3.2 3.3 3.5 子空间 子空间判定 逆矩阵 高斯消元 线性相关 矩阵乘法 转置 结合律 模拟卷"
    },
    {
     "id": "lectures",
     "title": "四讲复习提纲（L1–L4）",
     "file": "lectures/index.html",
     "full": "lectures-full.html",
     "desc": "按课次整理的完整笔记：方程组与消元、张成与无关、行空间与秩、子空间与矩阵运算，附 22 道自测题与思维导图。",
     "tags": [
      "讲义",
      "基础",
      "自测"
     ],
     "date": "2026-10-29",
     "pages": 26,
     "pdf": "MATH0280_复习提纲_手机版.pdf",
     "img": "mindmap-la-lectures.png",
     "keywords": "高斯消元 行阶梯形 REF 张成 span 线性无关 行空间 基 维数 秩 子空间 矩阵运算 转置 对称 逆矩阵"
    }
   ]
  },
  {
   "code": "math-modeling",
   "name": "数学建模 1",
   "en": "Mathematical Modeling 1",
   "course": "ENGSCI 111",
   "term": "2026 Fall",
   "teacher": "KP. Wang · Section 1",
   "color": "#1f7a8c",
   "accent": "teal",
   "scope": [
    "Assignment #5：图形判读（绝对/局部极值）",
    "闭区间上的绝对最值（EVT 三步法）",
    "含参数最值 x^a(1−x)^b",
    "单调性与局部极值（f′ 符号表）",
    "凹凸性与拐点（f″ 符号表）",
    "完整作图：f / f′ / f″ 信息表",
    "隐函数一阶导、二阶导",
    "切线方程 · Bessel 函数",
    "取对数求导与 arcsec 的导数"
   ],
   "exclude": [],
   "notes": "Assignment #5 共 14 题，8:15 am Nov 5 课堂交；本页按三条主线（形状 / 求导技巧 / 证明）重排，含全部步骤与速查表。",
   "docs": [
    {
     "id": "a5",
     "title": "Assignment #5 全解 · 极值与隐函数求导",
     "file": "a5/index.html",
     "full": "a5-full.html",
     "desc": "14 题逐题完整过程：图形极值判读、EVT 闭区间三步法、含参最值、单调/凹凸符号表、作图清单、隐函数与对数求导、arcsec 证明；另附一页纸速查表、标准答案汇总与十个高频失分点。",
     "tags": [
      "作业",
      "极值",
      "隐函数求导"
     ],
     "date": "2026-11-04",
     "pages": 12,
     "pdf": "ENGSCI111_Assignment5.pdf",
     "img": "engsci-p1-graph.png",
     "keywords": "极值 绝对最大 局部最小 图形判读 EVT 最值定理 单调性 凹性 拐点 三阶导 作图 隐函数求导 dy/dx y'' 切线 对数求导 arcsec sec^-1 取对数 临界点 符号表"
    }
   ]
  },
  {
   "code": "general-chemistry",
   "name": "普通化学",
   "en": "General Chemistry for Engineers 1",
   "course": "SCUPI",
   "term": "2026 Fall",
   "teacher": "Dr. Jue Gong · Section 1 · Sichuan University – Pittsburgh Institute",
   "color": "#7a51a6",
   "accent": "purple",
   "scope": [
    "Ch.1 测量：SI 单位、前缀、温度换算、有效数字、准确度与精密度",
    "Ch.1 物质的分类（元素/化合物/混合物）与强度/广延性质",
    "Ch.2 亚原子粒子、放射性、Thomson 与 Rutherford 模型",
    "Ch.2 原子序数、质量数、同位素与平均原子质量",
    "Ch.2 摩尔与摩尔质量（N_A、M、质量—摩尔—粒子数换算）",
    "Ch.3 光的波动性、光电效应、Bohr 能级与 Rydberg 公式",
    "Ch.3 de Broglie、不确定原理、一维势箱、Schrödinger 方程",
    "Ch.3 四个量子数、轨道形状、Aufbau/Pauli/Hund、电子排布与磁性",
    "Ch.4 有效核电荷 Zeff（Slater 规则）与周期趋势",
    "Ch.4 原子半径 / 电离能 / 电子亲和能 / 离子半径与等电子系列",
    "Ch.5 离子与分子化合物命名、晶格能、化学式、经验式与百分组成",
    "Ch.6 分子形状与极性（VSEPR、偶极矩、形式电荷、共振）",
    "Ch.6 分子间作用力（色散力 / 偶极 / 氢键 / 离子–偶极）",
    "Ch.7 价键理论、杂化（sp / sp² / sp³ / sp³d / sp³d²）、σ 与 π 键",
    "Ch.8 分子轨道理论、键级、磁性、离域键",
    "Ch.9 化学计量（限量试剂、产率）、浓度与稀释",
    "Ch.9 沉淀 / 酸碱 / 氧化还原、净离子方程、pH、滴定与重量分析"
   ],
   "exclude": [],
   "notes": "覆盖 Lecture 1–4 与 Lecture 7–9 全部课件，并对应 HW1–HW6。Blackboard 公告的期中考试为 2026-11-14。",
   "docs": [
    {
     "id": "notes",
     "title": "概念与公式总复习（Lecture 1–4, 7–9 ＋ HW1–6）",
     "file": "notes/index.html",
     "full": "notes-full.html",
     "desc": "九章一条主线：测量 → 原子组成 → 电子状态 → 周期趋势 → 命名与计量 → 分子形状与分子间作用力 → 价键与杂化 → 分子轨道 → 溶液中的反应。含 20+ 张对照表、公式速查表、30 条易错点、10 类题型模板、20 道自测题（附答案）。",
     "tags": [
      "讲义",
      "公式表",
      "自测"
     ],
     "date": "2026-11-13",
     "pages": 14,
     "keywords": "有效数字 SI单位 温度换算 同位素 平均原子质量 摩尔 阿伏伽德罗 光电效应 Bohr Rydberg de Broglie 不确定原理 势箱 量子数 电子排布 Aufbau Hund 泡利 顺磁 反磁 有效核电荷 Slater 原子半径 电离能 电子亲和能 离子半径 等电子 命名 含氧酸 水合物 经验式 百分组成 Lewis 形式电荷 共振 VSEPR 键角 偶极矩 极性 分子间作用力 氢键 色散力 价键理论 杂化 sp sp2 sp3 sigma pi 分子轨道 键级 离域 苯 限量试剂 产率 摩尔浓度 稀释 pH 电解质 沉淀 溶解度 净离子方程 酸碱 氧化还原 氧化数 活性顺序 滴定 重量分析"
    }
   ]
  }
 ]
};
