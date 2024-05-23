# A demo file on how to use Llama3 model to summarize a text and pick out the important parts.
import ollama

response = ollama.chat(model='llama3', messages=[
  {
    'role': 'user',
    'content': '''Can you please summarize the text below in a coherent manner:
        The government has been slow to implement a national school nutrition program, which was pushed for by the NDP. After three and a half years, millions of Canadian children have gone hungry. The Liberals have asked grocery stores to act, but what's needed is strong governmental action like a windfall profits tax on banks. A national school food program would ensure that kids never worry about their next meal or focus on school.

The Liberal Party of Canada is advertising a summer event featuring the Speaker, which promotes inflammatory language about the Conservative Party. The Speaker's local team organized the event, but the Speaker must take responsibility as he did not distance himself from it. This partisan behavior raises concerns about his impartiality and trustworthiness. As Speaker, he has repeatedly engaged in questionable partisan behavior, including attending a cocktail party and speaking at an Ontario Liberal Party leadership convention. The opposition has lost confidence in him, and the speaker is urged to vacate the chair and schedule a new election.

The text discusses the economic struggles faced by small businesses and families due to Liberal policies. MPs from various parties engage in a heated debate, with some accusing each other of being out of touch with reality. The Conservatives claim that Canada is not doing well economically, while the Liberals argue that Canada is performing reasonably well compared to other countries. The NDP points out that Canada is one of the only G7 countries without a national school food program, and that Conservative policies are driving up costs and making it harder for families to feed their children.

The speaker is concerned about a bill that combines privacy legislation with AI-related amendments. They believe the bill is flawed and should be split into two votes. The first part of the bill deals with privacy, particularly financial data, which they argue should be considered sensitive information. They also discuss the importance of ensuring AI cannot emulate human beings without consent. The speaker is worried that if the bill is not separated, it may not pass at all.

Previous governments have failed to address privacy rights and regulate artificial intelligence (AI). The Liberal government has panned its own budget and has not tabled parts of it that were discussed. The ethics committee worked on language to protect privacy rights in 2018-19 but nothing was implemented. The Privacy Commissioner said the government's legislation would undermine his ability to hold companies accountable. The government has also failed to double the Privacy Commissioner's budget, making enforcement impossible.

Note: This summary only includes the parts of the text that mention what previous governments have not done.

NDP member Peter Julian criticized Conservative MPs for blocking dental care and pharmacare legislation that would benefit seniors and others in their ridings. Minister Patty Hajdu responded by highlighting the government's investments in indigenous services, including education and post-secondary funding. She also criticized the Conservatives for obstructing important legislation at committee and emphasized the need to work together to improve Canadians' lives.

The text discusses various topics including a national food program, economic issues, and commemorations. The government has proposed a national food program to alleviate hunger among children, with the goal of ensuring no child is hungry while in school. Some MPs have expressed concerns about the state of the Canadian economy, citing a recent report showing Canada's GDP per capita has dropped 3% over four years. There are also tributes to individuals who have passed away and commemorations of historical events, such as the memory of the Patriots in Quebec.

The UN adopted some of Claude's research tools. MP Ryan Williams talked about the Liberal-NDP minority government being the longest-serving and Canadians facing poverty. MP Heath MacDonald recognized Nick Green, an island beef producer who won an environmental award. Leader Pierre Poilievre criticized the government for hiking carbon taxes and not addressing inflation. Deputy Prime Minister Chrystia Freeland defended the government's handling of inflation and debt, saying it was under control. The debate focused on economic issues, with Poilievre accusing the government of being incompetent and Freeland arguing that the country is doing well.

The carbon price is an effective way to address climate change while ensuring affordability for Canadians. The Conservatives should consider Premier Smith's experience, where her family received more money back than they paid in the price on pollution. They could ask her to reduce the price by 13┬ó, which she recently raised without a rebate.

(Note: I did not include any other topics or issues discussed in the original text.)

The government is introducing a budget that some argue interferes with Quebec's jurisdictions and threatens funding for housing, healthcare, and financial sectors. The Bloc Qu├⌐b├⌐cois is critical of the budget, while the Liberal government defends its implementation. The discussion also touches on healthcare, specifically the toxic drug crisis in British Columbia, and the introduction of the safe hospitals act.

John Allen Fraser, a Canadian politician, has passed away at age 92. He served as the Conservative MP for Vancouver South from 1972 to 1993 and was Speaker of the House from 1986 to 1994. Fraser was known for his kind, humorous, and wise nature. As Speaker, he was responsible for making decisions that are still cited today. He also served as Minister of Environment, Postmaster General, and Minister of Fisheries and Oceans. Colleagues praised his dedication, honesty, and ability to bring people together.

The government is taking bold action to address Canada's housing crisis, investing $1.5 billion in the Canada Rental Protection Fund and $6 billion in the Canada Housing Infrastructure Fund. The plan aims to unlock 3.87 million homes by 2031. Other measures include creating a Canadian Renters' Bill of Rights, increasing funding for secondary suites, and eliminating mandatory parking requirements near transit lines. This is part of a broader strategy to make life more affordable and drive economic growth that benefits all generations.

The Conservative party criticizes the Liberal budget for not addressing carbon emissions and promoting Canadian energy production. They argue that destroying the fossil fuel industry will harm Canadian prosperity and reduce carbon emissions. The Conservatives propose restoring Canada's competitive advantage by developing all renewable and non-renewable resources, which would also improve productivity and reduce spending. The opposition parties, including the NDP and Bloc Quebecois, criticize the Conservative party for not supporting social programs and for being tone-deaf to corporate profit increases.

Several MPs spoke during a budget debate. Madam Speaker (Conservative) highlighted the Liberal government's investment in manufacturing jobs and reviving Ontario's industrial heartland. Mrs. Julie Vignola (Bloc Qu├⌐b├⌐cois) criticized the budget for creating duplicate services in Quebec, disrespecting the Constitution, and not allowing provinces to opt out with full compensation. Mr. Irek Kusmierczyk (Conservative) emphasized the importance of teamwork and investing in clean-tech industries. Mr. Matthew Green (NDP) questioned the government's cuts to workforce development programs.

Here are the statistics mentioned in the text:

* Violent crime in Canada is up 39% since 2015.
* Homicides are up 43%, the highest rate in 30 years.
* Gang-related homicides are up 108%.
* Violent gun crimes are up 101%.
* Assault with a weapon is up 61%.
* Sexual assault has increased 71% since 2015.
* Sex crimes against children are up 126%.
* Auto theft is out of control, with no specific percentage mentioned.
* The rate of extortion in Canada has increased 218% since 2015.
* Police-reported extortion increased 39% in a single year (2022).
* The rate of extortion in Ontario is up 263%, in Alberta it's up 284%, and in British Columbia it's up 386% since 2015.

Conservative MP Tim Uppal spoke about Bill C-23, which aims to restore mandatory minimum penalties for certain crimes, such as extortion with a firearm. He emphasized the need for tougher laws to combat crime, citing statistics showing a 39% increase in crime since the Liberal government took power. Uppal also mentioned that Canadians of Sikh faith gather weekly at a national historic site to worship and shared meals with him. He urged all members of Parliament to support the bill, which is a response to constituents' requests for safer streets.

The government is investing in critical minerals to make Canada a leader in EV manufacturing and creating jobs. The Conservatives are sticking their heads in the sand, saying they don't need a plan for pollution or investments. In contrast, the government is taking action by investing in workers and infrastructure, which has attracted international companies. Additionally, the budget includes measures to increase rental housing and simplify the building process. The government is committed to solving the housing crisis and is proposing new ideas to make it happen.

The speaker criticizes the government for not highlighting successful initiatives, such as the $10-million exemption for farm business sales to employee ownership trusts. They also express disappointment with the budget, citing omissions like the emergency on-farm support fund and investment in agri-food. The speaker calls for a permanent advance payments program and an agile emergency fund. They also highlight the importance of indigenous communities having access to clean drinking water.

Canadian voters are expressing frustration with the government's budget proposal, calling it "unpopular" and "out of touch." They want to see a balanced budget and reduced debt, rather than increased taxes. The government's plan to introduce a new federal property tax is seen as an attack on property rights and a way for wealthy Canadians to avoid paying taxes. The text also criticizes the government's handling of taxes, accusing it of being incompetent and ignoring the Charter of Rights and Freedoms.
focusing on the entire community and ecoregion around the Salish Sea:

The text does not mention the Salish Sea or any environmental concerns. Instead, it discusses a budget debate in Canada's Parliament, specifically highlighting issues related to reproductive rights, pharmacare, and poverty reduction. The speaker, Leah Gazan, criticizes the Conservative Party for voting against access to free contraception and abortion care, while praising the NDP's efforts to establish a national school food program and pharmacare. She also expresses disappointment with the Liberal government's failure to address these issues.
focusing on helping seniors and setting up Canadians for a good future:

The Bloc Qu├⌐b├⌐cois and Liberal parties have invested in housing programs to help Canadians and Quebecers. The government has also launched the new Canada disability benefit and is investing in housing for people with disabilities. In contrast, the Conservative Party criticizes the budget for not providing enough tax relief, failing to restore affordability, and increasing national debt. They argue that the budget does not address the needs of everyday Canadians and fails to provide a solution to the housing crisis.

The Liberal government has taken steps to combat climate change and address housing affordability issues. However, the Bloc Qu├⌐b├⌐cois criticizes the government's handling of taxation, banking, and provincial jurisdiction. The Bloc wants Quebec to have the right to opt out of federal programs and receive full compensation, as well as an increase in old age security and an end to fossil fuel subsidies. The government has not met these requests, instead choosing to accumulate debt and impose conditions on provinces and municipalities.

A Conservative MP argues that their party has been violating a clear ruling from 10 years ago by questioning the Speaker's impartiality and raising false allegations. They claim that this is an attempt to skirt the rules of the House, which has resulted in numerous violations. The MP requests that the Speaker investigate these breaches and take action.

Here are the alleged violations:

* Conservative MPs questioning the Speaker's impartiality
* Raising false allegations against the Speaker
* Violating the principle of not questioning the Speaker's impartiality

These violations allegedly occurred over a period of 10 years, starting from a ruling by a former Speaker.

The text discusses ways to increase affordable housing in Canada. The Housing Accelerator Fund provides federal dollars for communities that pledge to change zoning laws to allow for middle-class housing. Modular home building is also mentioned as a potential solution, with factories producing homes quickly and efficiently. Some members of parliament are calling for the removal of the GST on construction costs and carbon taxes to encourage more building.

Called for:

* Housing Accelerator Fund
* Changing zoning laws to allow for middle-class housing
* Removing GST on construction costs
* Carbon tax reduction or elimination
* Modular home building as a solution for affordable housing

The member speaks about various provisions in the budget, including pharmacare, which will help millions of Canadians with diabetes and other conditions. They also discuss the national school food program, which would benefit nearly half a million kids, but is being blocked by Conservatives. The member criticizes the Liberal government for maintaining some negative practices from the Harper regime, such as tax haven treaties that cost Canada $30 billion annually.

The text does not mention a specific budget that puts money into the national school food program. However, it appears to reference the government's budget bill (Bill ) which is being debated in the House.

The main speaker, Jenica Atwin, mentions that the Canada she envisions 10 years from now would include investments and support for Canadians, but does not specifically mention a budget allocation for the national school food program.

The speaker argues that Conservatives were wrong about inflation increasing due to government spending. Inflation has remained within the Bank of Canada's target range of 2% to 3%. The speaker also criticizes Conservative claims that investing in Canadians contributed to inflation, and notes that experts said otherwise. The speaker highlights several initiatives from the fall economic statement, including affordable housing projects and a tax-free first home savings account, which have helped many Canadians.

The government has shown a lack of common sense, leading to increased taxes (up 23% \on April 1), rising costs, and a housing shortage. The government has approved mergers that have led to higher mortgage rates and reduced competition. They have also failed to contribute to international security efforts through NATO and NORAD, and neglected Canada's north with only one functioning icebreaker compared to Russia's 16 and China's 40. The author calls for a common-sense Conservative government to restore sanity in Canada.

Conservative MP speaks about concerns over government debt, housing affordability, and food banks in Saskatchewan. He blames the Liberal government for neglecting the province. Other MPs discuss issues such as the Conservative Party's performance in Quebec and the need to address high gas prices. One MP criticizes the Conservatives for giving a "free ride" to oil and gas companies, while another questions why the Liberals charge GST on top of carbon tax, making life more expensive for Canadians.

Here are the questions being asked:

* Will the government finally list the IRGC as a terrorist organization and shut down its operations? Yes or no?
* (Multiple times) What is the government's strategy to address the overdose crisis, particularly in British Columbia?
* How will the government ensure that Canadians have access to a full range of options for prevention, risk reduction, treatment, and recovery services?

Note that these are not direct quotes from the text, but rather paraphrased summaries of the questions being asked.
''',
  },
])

print(response['message']['content'])