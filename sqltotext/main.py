import streamlit as st
import get_sql_query
import execute_sql_query

def main():
    st.title('SQL Query Generator and Executor')

    # User input for natural language query
    user_query = st.text_input('Enter your natural language query:', '')

    if st.button('Generate and Execute SQL'):
        if user_query:
            # Generate the SQL query from natural language
            schema_prompt = """
    use call_data;
    CREATE TABLE chr20250205_subset (
        callid INT, acwtime INT, ansholdtime INT, consulttime INT, duration INT,
        segstart DATETIME, segstart_utc DATETIME, segstop DATETIME, segstop_utc DATETIME,
        talktime INT, netintime INT, origholdtime INT, queuetime INT, ringtime INT,
        tenant_num INT, ecd_num INT, dispivector VARCHAR(255), dispsplit INT,
        firstivector VARCHAR(255), split1name VARCHAR(255), split2name VARCHAR(255),
        split3name VARCHAR(255), tkgrp VARCHAR(255), eqloc VARCHAR(255),
        orig_locid VARCHAR(255), ans_locid VARCHAR(255), obs_locid VARCHAR(255),
        uui_len INT, assist INT, audio INT, conference INT, da_queued INT,
        holdabn INT, malicious INT, observingcall INT, transferred INT,
        agt_released INT, acd INT, call_disposition_type VARCHAR(255),
        dispriority INT, held INT, segment INT, ansreason VARCHAR(255),
        origreason VARCHAR(255), dispsklevel INT, event1 INT, event2 INT,
        event3 INT, event4 INT, event5 INT, event6 INT, event7 INT,
        event8 INT, event9 INT, ecd_control VARCHAR(255), ecd_info TEXT,
        ucid VARCHAR(255), dispvdn VARCHAR(255), firstvdn VARCHAR(255),
        origlogin VARCHAR(255), anslogin VARCHAR(255), lastobserver VARCHAR(255),
        dialednum VARCHAR(255), calling_pty VARCHAR(255), lastdigits VARCHAR(255),
        lastcwc VARCHAR(255), calling_ii VARCHAR(255), cwc1 VARCHAR(255),
        cwc2 VARCHAR(255), cwc3 VARCHAR(255), cwc4 VARCHAR(255), cwc5 VARCHAR(255),
        vdn2 VARCHAR(255), vdn3 VARCHAR(255), vdn4 VARCHAR(255), vdn5 VARCHAR(255),
        vdn6 VARCHAR(255), vdn7 VARCHAR(255), vdn8 VARCHAR(255), vdn9 VARCHAR(255),
        asai_uui VARCHAR(255), interuptdel INT, agentsurplus INT, agentskilllevel INT,
        prefskilllevel INT, icrresent INT, icrpullreason INT, orig_attrib_id VARCHAR(255),
        ans_attrib_id VARCHAR(255), obs_attrib_id VARCHAR(255), ecd_str TEXT
    );
    """
            sql_query = get_sql_query.get_sql_query(user_query, schema_prompt)

            if sql_query:
                print(f"Generated SQL Query: {sql_query}")
                results = execute_sql_query.execute_sql_query(sql_query)
                if results:
                    #st.write('Database Results:', results)

                    # Translate results to natural language
                    answer = execute_sql_query.translate_results_to_natural_language(results, user_query)
                    st.write('Natural Language Answer:', answer)
                else:
                    st.error("No data returned from the database or query execution failed.")
            else:
                st.error("Failed to generate SQL query or invalid response format.")
        else:
            st.error("Please enter a query to proceed.")

if __name__ == '__main__':
    main()
