import streamlit as st
from math import ceil
import pickle

st.set_page_config(layout="wide")


try:
    menu_item = st.session_state.menu_items[st.session_state["menu_item"]]
    menu_item_name = menu_item["name"]
    st.query_params['item'] = menu_item["name"]
except AttributeError:
    menu_item_name = st.query_params['item']
    st.session_state.dialog_shown = True

# functions for pickle stuff
def store_data(ratings_dict: dict[str, dict[int, int]]):

    ratings_file = open('example_ratings', 'wb')
    pickle.dump(ratings_dict, ratings_file)
    ratings_file.close()


def load_data() -> dict:

    ratings_file = open('example_ratings', 'rb')
    ratings = pickle.load(ratings_file)
    # for keys in ratings:
    #     print(keys, '=>', ratings[keys])
    ratings_file.close()
    return ratings


def avg_rating(ratings):

    review_sum = 0
    num_reviews_sum = 0
    for key in ratings[menu_item_name]:
        review_sum += ratings[menu_item_name][key]*key
        num_reviews_sum += ratings[menu_item_name][key]
    return (review_sum/num_reviews_sum), num_reviews_sum


def render_rating_bar(num_stars, rating_percentage, num_reviews):
    bar_html = f"""
    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 10px;">
      <div style="font-size: 14px; font-family: Arial, sans-serif; display: flex; align-items: center; gap: 4px;">
        <span>{num_stars}</span>
        <span style="display: inline-block; font-size: 14px; color: #f1c328; line-height: 1;">&#9733;</span>
      </div>
      <div style="flex-grow: 1; width: 100%; border: 1px solid #ddd; border-radius: 10px; overflow: hidden; background-color: #f5f5f5; height: 12px;">
        <div style="width: {rating_percentage}%; height: 100%; background-color: #ffbd44; border-radius: 10px;">
        </div>
      </div>
      <div style="font-size: 14px;">{num_reviews}</div>
    </div>
    """
    st.markdown(bar_html, unsafe_allow_html=True)


st.title("Nutrition and Reviews")
st.write("---")
st.header(menu_item_name)

col1, col2 = st.columns([0.4, 0.6])

with col1:
    with st.container(border=False):
        st.write(
            """
            <style>

.performance-facts {
  font-size: small;
            line-height: 1.4;
            color: black;
  border: 1px solid black;
  background: white;
  margin: 20px;
  float: left;
  width: 335px;
  padding: 0.5rem;
  table {
    border-collapse: collapse;
  }
}
.performance-facts__title {
  font-weight: bold;
  font-size: 2rem;
  margin: 0;
  padding: 0;
  h1 {
            padding: 0 !important;
            }
}

.performance-facts__header {
  border-bottom: 10px solid black;
  padding: 0;
  margin: 0;
  p {
    margin: 0;
  }
}
           .performance-facts p {
            margin: 0px;
            }

.performance-facts__table {
  width: 100%;
  thead tr {
    th,
    td {
      border: 0;
    }
  }
  th,
  td {
    font-weight: normal;
    text-align: left;
    padding: 0.25rem 0;
    border-top: 0.1rem solid black;
    white-space: nowrap;
  }
  td {
    &:last-child {
      text-align: right;
    }
  }
  .blank-cell {
    width: 1rem;
    border-top: 0;
  }
  .thick-row {
    th,
    td {
      border-top-width: 5px;
    }
  }
}
.small-info {
  font-size: 0.7rem;
}

.performance-facts__table--small {
  @extend .performance-facts__table;
  border-bottom: 1px solid #999;
  margin: 0 0 0.5rem 0;
  thead {
    tr {
      border-bottom: 1px solid black;
    }
  }
  td {
    &:last-child {
      text-align: left;
    }
  }
  th,
  td {
    border: 0;
    padding: 0;
  }
}

.performance-facts__table--grid {
  @extend .performance-facts__table;
  margin: 0 0 0.5rem 0;
  td {
    &:last-child {
      text-align: left;
      &::before {
        content: "•";
        font-weight: bold;
        margin: 0 0.25rem 0 0;
      }
    }
  }
}

.text-center {
  text-align: center;
}
.thick-end {
  border-bottom: 10px solid black;
}
.thin-end {
  border-bottom: 1px solid black;
}
            </style>

            """,
            unsafe_allow_html = True)

        st.markdown(
            f"""

<section class="performance-facts">
  <header class="performance-facts__header">
    <h1 class="performance-facts__title", style="padding:0;">Nutrition Facts</h1>
    <p>Serving Size: 100g
      <p>Serving Per Container: 2</p>
  </header>
  <table class="performance-facts__table">
    <thead>
      <tr>
        <th colspan="3" class="small-info">
          Amount Per Serving
        </th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <th colspan="2">
          <b>Calories</b>
          1000
            </th>
        <td>
          Calories from Fat
          500
        </td>
      </tr>
      <tr class="thick-row">
        <td colspan="3" class="small-info">
          <b>% Daily Value*</b>
        </td>
      </tr>
      <tr>
        <th colspan="2">
          <b>Total Fat</b>
          18g
        </th>
        <td>
          <b>30%</b>
        </td>
      </tr>
      <tr>
        <td class="blank-cell">
        </td>
        <th>
          Saturated Fat
          15g
        </th>
        <td>
          <b>15%</b>
        </td>
      </tr>
      <tr>
        <td class="blank-cell">
        </td>
        <th>
          Trans Fat
          11g
        </th>
        <td>
        </td>
      </tr>
      <tr>
        <th colspan="2">
          <b>Cholesterol</b>
          13g
        </th>
        <td>
          <b>8%</b>
        </td>
      </tr>
      <tr>
        <th colspan="2">
          <b>Sodium</b>
          100g
        </th>
        <td>
          <b>15%</b>
        </td>
      </tr>
      <tr>
        <th colspan="2">
          <b>Total Carbohydrate</b>
          8g
        </th>
        <td>
          <b>30%</b>
        </td>
      </tr>
      <tr>
        <td class="blank-cell">
        </td>
        <th>
          Dietary Fiber
          82g
        </th>
        <td>
          <b>19%</b>
        </td>
      </tr>
      <tr>
        <td class="blank-cell">
        </td>
        <th>
          Sugars
          14g
        </th>
        <td>
        </td>
      </tr>
      <tr class="thick-end">
        <th colspan="2">
          <b>Protein</b>
          5g
        </th>
        <td>
        </td>
      </tr>
    </tbody>
  </table>


  <p class="small-info">* Percent Daily Values are based on a 2,000 calorie diet. Your daily values may be higher or lower depending on your calorie needs:</p>
</section>
            """,
           unsafe_allow_html=True)


with (col2):
    st.write("")
    sub_col1, sub_col2 = st.columns([0.6, 0.4])
    ratings = load_data()
    with sub_col1:
        st.subheader("Leave a rating!")
        selected = st.feedback("stars")

        if selected is not None:
            selected += 1
            st.write(f"You left a {selected} star review!")

            # update ratings
            ratings[menu_item_name][selected] += 1
            store_data(ratings)

        with sub_col2:
            avg, review_sum = avg_rating(ratings)
            st.write(f"{round(avg, 2)} stars on average")
            for i in range(5, 0, -1):
                reviews_for_i_stars = ratings[menu_item_name][i]
                percentage = round(reviews_for_i_stars/review_sum,2)*100
                render_rating_bar(i, percentage, reviews_for_i_stars)
            st.write(" ")
            st.write(" ")
            if st.button("Back"):
                st.switch_page("main.py")

