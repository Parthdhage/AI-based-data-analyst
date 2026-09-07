

GROUP_BY_TOOL = {
      "type": "function",
      "function": {
        "name": "group_by",
        "description": ("Group rows by a category column and compute a single aggregate "
            "value for each group. Use for questions like 'total revenue by "
            "region', 'average price per category', or 'how many orders per "
            "customer'."),
        "parameters": {
          "type": "object",
          "properties": {
            "group_column": {
              "type": "string",
              "description": ("Name of the column to group by. Must be a category "
                        "column with repeated values, such as region or product.")
            },
            "value_column": {
              "type": "string",
              "description": ("Name of the numeric column to aggregate, such as "
                        "revenue or quantity.")
            },
            "how": {
              "type": "string",
              "enum": ["sum", "mean", "min", "max", "std", "count"],
              "description": "The aggregation to apply to value_column."
            },
          },
          "required":["group_column", "value_column", "how"]
        }
      }
    }
TIME_TREND_TOOL =  {
      "type": "function",
      "function": {
        "name": "time_trend",
        "description": ("Track how a numeric value changes over time by grouping rows "
            "into time periods. Use for questions about trends, growth, or "
            "change over time, such as 'monthly revenue', 'how did sales "
            "change this year', 'daily order count', or 'revenue trend by "
            "quarter'. Requires a column containing dates."),
        "parameters": {
          "type": "object",
          "properties": {
            "date_column": {
              "type": "string",
              "description": ( "Name of the column containing dates or timestamps. "
                        "Rows whose dates cannot be parsed are excluded and "
                        "reported separately in the result.")
            },
            "value_column": {
              "type": "string",
              "description": ("Name of the numeric column to aggregate within each "
                        "time period, such as revenue or quantity.")
            },
            "how": {
              "type": "string",
              "enum": ["sum", "mean", "min", "max", "std", "count"],
              "description": "The aggregation to apply to value_column within each "
                        "time period."
            },
            "freq": {
              "type": "string",
              "enum": ["D", "W", "M", "Q", "Y"],
              "description": "Size of each time bucket: D for daily, W for weekly, "
                        "M for monthly, Q for quarterly, Y for yearly."
            },
          },
          "required":["group_column", "value_column", "how", "freq"],
        }
      }
    }
  

TOP_N_TOOL = {
    "type": "function",
    "function": {
        "name": "top_n",
        "description": (
            "Rank categories by an aggregated value and return only the "
            "highest or lowest few. Use for questions about bests, worsts, or "
            "rankings, such as 'top 5 products by revenue', 'which regions "
            "sell the least', or 'my three biggest customers'. Prefer this "
            "over group_by when the user asks for a limited number of results."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "group_column": {
                    "type": "string",
                    "description": (
                        "Name of the category column to rank, such as product "
                        "or region."
                    ),
                },
                "value_column": {
                    "type": "string",
                    "description": (
                        "Name of the numeric column to rank by, such as "
                        "revenue or quantity."
                    ),
                },
                "how": {
                    "type": "string",
                    "enum": ["sum", "mean", "min", "max", "std", "count"],
                    "description": "The aggregation to apply to value_column.",
                },
                "n": {
                    "type": "integer",
                    "minimum": 1,
                    "description": (
                        "How many results to return. Use the number the user "
                        "asked for, or 5 if they did not specify."
                    ),
                },
                "direction": {
                    "type": "string",
                    "enum": ["top", "bottom"],
                    "description": (
                        "Use 'top' for highest values (best, most, largest) "
                        "and 'bottom' for lowest values (worst, least, "
                        "smallest)."
                    ),
                },
            },
            "required": ["date_column", "value_column", "how", "freq"],
        },
    },
}
TOOLS = [GROUP_BY_TOOL, TIME_TREND_TOOL, TOP_N_TOOL]

#  "messages": [
 ##    "role": "system",
  #    "content": "You are a weather assistant. Respond to the user question and use tools if needed to answer the query."
 #  ]