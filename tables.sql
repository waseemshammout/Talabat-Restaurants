/*
    URLs table creation
*/

CREATE TABLE talabat_restaurants_urls(
	[id] [int] IDENTITY(1,1) NOT NULL,
	[url] [nvarchar](4000) NULL,
	[done] [bit] NULL,
	[page_active] [bit] NULL,
 CONSTRAINT [PK_talabat_restaurants_urls] PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY];

/*
    Restaurants fact table creation
*/
CREATE TABLE talabat_restaurants(
	[id] [int] IDENTITY(1,1) NOT NULL,
	[entry_name] [nvarchar](255) NULL,
	[category] [nvarchar](250) NULL,
	[rating] [float] NULL,
	[rated] [int] NULL,
	[reviewed] [int] NULL,
	[descriptive_message] [text] NULL,
	[link_id] [int] NULL,
 CONSTRAINT [PK_talabat_restaurants] PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY];

