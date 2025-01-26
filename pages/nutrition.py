import streamlit as st
from math import ceil
import pickle

menu_item = st.session_state.menu_items[st.session_state["menu_item"]]

# functions for pickle stuff

# back up ratings for testing
# keys are of the form # stars: # ratings for that num of stars
# ratings = {"Turkey BLT": {5:13, 4:12, 3:11, 2:10, 1:9},
#         "Cheese Pizza" : {5:23, 4:22, 3:21, 2:20, 1:19},
#         "Sausage Pizza" : {5:33, 4:32, 3:31, 2:30, 1:29},
#         "Cheeseburger" : {5:43, 4:42, 3:41, 2:40, 1:39},
#         }


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
    for key in ratings[menu_item["name"]]:
        review_sum += ratings[menu_item["name"]][key]*key
        num_reviews_sum += ratings[menu_item["name"]][key]
    return (review_sum/num_reviews_sum), num_reviews_sum


st.set_page_config(layout="wide")

st.title("Nutrition and Reviews")
st.write("---")
st.header(menu_item["name"])

col1, col2 = st.columns([0.4, 0.6])

with col1:
    with st.container(border=False):
#         st.write(
#             """
#             <style>
#
# .performance-facts {
#   font-size: small;
#             line-height: 1.4;
#             color: black;
#   border: 1px solid black;
#   background: white;
#   margin: 20px;
#   float: left;
#   width: 335px;
#   padding: 0.5rem;
#   table {
#     border-collapse: collapse;
#   }
# }
# .performance-facts__title {
#   font-weight: bold;
#   font-size: 2rem;
#   margin: 0;
#   padding: 0;
#   h1 {
#             padding: 0 !important;
#             }
# }
#
# .performance-facts__header {
#   border-bottom: 10px solid black;
#   padding: 0;
#   margin: 0;
#   p {
#     margin: 0;
#   }
# }
#            .performance-facts p {
#             margin: 0px;
#             }
#
# .performance-facts__table {
#   width: 100%;
#   thead tr {
#     th,
#     td {
#       border: 0;
#     }
#   }
#   th,
#   td {
#     font-weight: normal;
#     text-align: left;
#     padding: 0.25rem 0;
#     border-top: 0.1rem solid black;
#     white-space: nowrap;
#   }
#   td {
#     &:last-child {
#       text-align: right;
#     }
#   }
#   .blank-cell {
#     width: 1rem;
#     border-top: 0;
#   }
#   .thick-row {
#     th,
#     td {
#       border-top-width: 5px;
#     }
#   }
# }
# .small-info {
#   font-size: 0.7rem;
# }
#
# .performance-facts__table--small {
#   @extend .performance-facts__table;
#   border-bottom: 1px solid #999;
#   margin: 0 0 0.5rem 0;
#   thead {
#     tr {
#       border-bottom: 1px solid black;
#     }
#   }
#   td {
#     &:last-child {
#       text-align: left;
#     }
#   }
#   th,
#   td {
#     border: 0;
#     padding: 0;
#   }
# }
#
# .performance-facts__table--grid {
#   @extend .performance-facts__table;
#   margin: 0 0 0.5rem 0;
#   td {
#     &:last-child {
#       text-align: left;
#       &::before {
#         content: "•";
#         font-weight: bold;
#         margin: 0 0.25rem 0 0;
#       }
#     }
#   }
# }
#
# .text-center {
#   text-align: center;
# }
# .thick-end {
#   border-bottom: 10px solid black;
# }
# .thin-end {
#   border-bottom: 1px solid black;
# }
#             </style>
#
#             """,
#             unsafe_allow_html = True)
#         st.markdown(
#             f"""
#
# <section class="performance-facts">
#   <header class="performance-facts__header">
#     <h1 class="performance-facts__title", style="padding:0;">Nutrition Facts</h1>
#     <p>Serving Size {menu_item['serving_size']}
#       <p>Serving Per Container 8 TODO</p>
#   </header>
#   <table class="performance-facts__table">
#     <thead>
#       <tr>
#         <th colspan="3" class="small-info">
#           Amount Per Serving
#         </th>
#       </tr>
#     </thead>
#     <tbody>
#       <tr>
#         <th colspan="2">
#           <b>Calories</b>
#           {menu_item['calories']}
#             </th>
#         <td>
#           Calories from Fat
#           TODO
#         </td>
#       </tr>
#       <tr class="thick-row">
#         <td colspan="3" class="small-info">
#           <b>% Daily Value*</b>
#         </td>
#       </tr>
#       <tr>
#         <th colspan="2">
#           <b>Total Fat</b>
#           {menu_item['total_fat']}g
#         </th>
#         <td>
#           <b>{ceil(menu_item['total_fat']/78 * 100)}%</b>
#         </td>
#       </tr>
#       <tr>
#         <td class="blank-cell">
#         </td>
#         <th>
#           Saturated Fat
#           {menu_item['saturated_fat']}g
#         </th>
#         <td>
#           <b>{ceil(menu_item['saturated_fat'] / 22 * 100)}%</b>
#         </td>
#       </tr>
#       <tr>
#         <td class="blank-cell">
#         </td>
#         <th>
#           Trans Fat
#           TODO
#         </th>
#         <td>
#         </td>
#       </tr>
#       <tr>
#         <th colspan="2">
#           <b>Cholesterol</b>
#           TODO
#         </th>
#         <td>
#           <b>TODO</b>
#         </td>
#       </tr>
#       <tr>
#         <th colspan="2">
#           <b>Sodium</b>
#           TODO
#         </th>
#         <td>
#           <b>TODO</b>
#         </td>
#       </tr>
#       <tr>
#         <th colspan="2">
#           <b>Total Carbohydrate</b>
#           TODO
#         </th>
#         <td>
#           <b>TODO</b>
#         </td>
#       </tr>
#       <tr>
#         <td class="blank-cell">
#         </td>
#         <th>
#           Dietary Fiber
#           TODO
#         </th>
#         <td>
#           <b>TODO</b>
#         </td>
#       </tr>
#       <tr>
#         <td class="blank-cell">
#         </td>
#         <th>
#           Sugars
#           TODO
#         </th>
#         <td>
#         </td>
#       </tr>
#       <tr class="thick-end">
#         <th colspan="2">
#           <b>Protein</b>
#           TODO
#         </th>
#         <td>
#         </td>
#       </tr>
#     </tbody>
#   </table>
#
#
#   <p class="small-info">* Percent Daily Values are based on a 2,000 calorie diet. Your daily values may be higher or lower depending on your calorie needs:</p>
# </section>
#             """,
#             unsafe_allow_html=True,
#         )    st.write("stand in")
        st.write("stand in")

    with st.container():
        if st.button("back"):
            st.switch_page("main.py")

with (col2):
    st.subheader("Leave a rating!")
    with st.container():
        col1, col2= st.columns([0.7, 0.3])
        ratings = load_data()
        with col1:
            selected = st.feedback("stars", key="rating_stars")
            if selected is not None:
                selected += 1
                # see streamlit documentation to see if we can use the named parameter "key" to
                # prevent multiple ratings without refreshing the page
                st.write(":red[TO FIX:  TIME YOU CHANGE THE STARS IT'S ADDED TO THE RECORD]")

        # changing the ratings dict
        if selected is not None:
            ratings[menu_item["name"]][selected] += 1
            store_data(ratings)

        with col2:
            avg, review_sum = avg_rating(ratings)
            st.feedback("stars", disable_with_feedback=4)
            st.write(f"{round(avg, 2)} stars on average")
            st.write(f"{review_sum} total reviews")