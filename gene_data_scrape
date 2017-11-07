import quiverpackage
import os

directory_name = os.path.dirname(__file__)

quiver_db_file = os.path.join(directory_name, "quiver_database.db")

conn = quiver.quiver_api.QuiverDB(quiver_db_file)

supplied_genes = 'ABL1', 'ABL2', 'ALK', 'BCL11B', 'BCL2', 'BCL3', 'BCL6', 'BCR', 'BIRC3', 'CBFB', 'CCND1', 'CCND3', \
                 'CDK6', 'CEBPG', 'CHD1', 'CHIC2', 'CIITA', 'CREBBP', 'CRLF2', 'CSF1R', 'DEK', 'DUSP22', 'EBF1', \
                 'EIF4A1', 'EPOR', 'ERG', 'ETV6', 'FGFR1', 'GLIS2', 'IKZF1', 'IKZF2', 'IKZF3', 'JAK2', 'KAT6A', \
                 'KLF2', 'KMT2A', 'MALT1', 'MECOM', 'MKL1', 'MLF1', 'MLLT10', 'MLLT4', 'MYC', 'MYD88', 'MYH11', \
                 'NF1', 'NFKB2', 'NOTCH1', 'NTRK3', 'NUP214', 'NUP98', 'P2PR8', 'P2RY8', 'PAG1', 'PAX5', 'PBX1', \
                 'PDCD1LG2', 'PDGFRA', 'PDGFRB', 'PICALM', 'PML', 'PRDM16', 'PTK2B', 'PYRY8', 'RARA', 'RBM15', \
                 'ROS1', 'RUNX1', 'RUNX1T1', 'SEMA6A', 'SETD2', 'STIL', 'TAL1', 'TCF3', 'TFG', 'TP63', 'TYK2',\
                 'ZCCHC7'

def main():

    gene_file = open('Gene_Fusions_Data', 'w')
    header = ['Supplied Target', 'Fusion Partner', 'Canonical Name', 'Supplied Target Panels', 'Fusion Partner Panels']

    gene_file.write('\t'.join(header) + '\n')

    for x in supply_gene_targets():
        gene_file.write('\t'.join(map(str, x)) + '\n')

    gene_file.write("\nData contains {} gene fusions.".format(len(supply_gene_targets())))

def supply_gene_targets():
    """
    :param: none
    :return: List of supplied genes, partner genes, canonical name, supplied target panel, fusion partner panel
    """
    fusion_query = "SELECT DISTINCT Known_Fusions.ApprovedGeneOrder " \
                   "FROM Known_Fusions WHERE ApprovedGeneOrder LIKE ?"

    final_results = []

    for gene in supplied_genes:
        fusion = conn.query(fusion_query, ("%{}%".format(gene),))

        for pair in fusion:
            genes = str(pair[0]).split(':')

            if len(genes) == 2:
                gene1, gene2 = genes
            else:
                gene1, gene2 = set(genes)

            if gene1 == gene:
                supp_target, partner = gene1, gene2
            elif gene2 == gene:
                supp_target, partner = gene2, gene1
            else:
                continue

            final_results.append([gene, partner, supp_target, target_partner_panel(supp_target),
                                  target_partner_panel(partner)])

    return final_results

def target_partner_panel(gene):
    """
    :param gene: supplied genes and partner genes
    :return: String of supplied target panels and fusion partner panels
    """
    panel_query = "SELECT DISTINCT Panel_Gene_List.PanelName FROM Panel_Gene_List " \
                  "WHERE Panel_Gene_List.GeneName = ? AND Panel_Gene_List.PanelName != ''"

    supplied_target_kits = conn.query(panel_query, ("{}".format(gene),))

    return ','.join([str(tup[0]) for tup in supplied_target_kits])

if __name__ == '__main__':
    main()
